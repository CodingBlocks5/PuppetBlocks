#
#   @file : Audio.py
#   @authors : PuppetBlocks team
#   @date : 21 February 2023
#
# This code is originally based on:
#   https://github.com/miketeachman/micropython-i2s-examples/blob/master/examples/wavplayer.py
#   https://github.com/miketeachman/micropython-i2s-examples/blob/master/examples/easy_wav_player.py
# Originally released under MIT license.
#
import struct
from machine import I2S, Pin

class Player:
    PLAY = 0
    PAUSE = 1
    RESUME = 2
    FLUSH = 3
    STOP = 4

    def __init__(self, id, sck_pin, ws_pin, sd_pin, ibuf, root="/sd/PuppetBlocks"):
        self.id = id
        self.sck_pin = sck_pin
        self.ws_pin = ws_pin
        self.sd_pin = sd_pin
        self.ibuf = ibuf
        self.root = root.rstrip("/") + "/"
        self.state = Player.STOP
        self.wav = None
        self.loop = False
        self.format = None
        self.sample_rate = None
        self.bits_per_sample = None
        self.first_sample_offset = None
        self.num_read = 0
        self.sbuf = 1000
        self.nflush = 0
        self.silence_samples = bytearray(self.sbuf)
        self.wav_samples_mv = memoryview(bytearray(10000))

    def i2s_callback(self, arg):
        if self.state == Player.PLAY:
            self.num_read = self.wav.readinto(self.wav_samples_mv)
            if self.num_read == 0:
                if self.loop == False:
                    self.state = Player.FLUSH
                else:
                    _ = self.wav.seek(self.first_sample_offset)
                _ = self.audio_out.write(self.silence_samples)
            else:
                _ = self.audio_out.write(self.wav_samples_mv[: self.num_read])
        elif self.state == Player.RESUME:
            self.state = Player.PLAY
            _ = self.audio_out.write(self.silence_samples)
        elif self.state == Player.PAUSE:
            _ = self.audio_out.write(self.silence_samples)
        elif self.state == Player.FLUSH:
            if self.nflush > 0:
                self.nflush -= 1
                _ = self.audio_out.write(self.silence_samples)
            else:
                self.wav.close()
                self.audio_out.deinit()
                self.state = Player.STOP
        elif self.state == Player.STOP:
            pass
        else:
            raise SystemError("Internal error:  unexpected state")

    def parse(self, wav_file):
        chunk_ID = wav_file.read(4)
        if chunk_ID != b"RIFF":
            raise ValueError("WAV chunk ID invalid")
        chunk_size = wav_file.read(4)
        format = wav_file.read(4)
        if format != b"WAVE":
            raise ValueError("WAV format invalid")
        sub_chunk1_ID = wav_file.read(4)
        if sub_chunk1_ID != b"fmt ":
            raise ValueError("WAV sub chunk 1 ID invalid")
        sub_chunk1_size = wav_file.read(4)
        audio_format = struct.unpack("<H", wav_file.read(2))[0]
        num_channels = struct.unpack("<H", wav_file.read(2))[0]
        if num_channels == 1:
            self.format = I2S.MONO
        else:
            self.format = I2S.STEREO
        self.sample_rate = struct.unpack("<I", wav_file.read(4))[0]
        byte_rate = struct.unpack("<I", wav_file.read(4))[0]
        block_align = struct.unpack("<H", wav_file.read(2))[0]
        self.bits_per_sample = struct.unpack("<H", wav_file.read(2))[0]
        binary_block = wav_file.read(200)
        offset = binary_block.find(b"data")
        if offset == -1:
            raise ValueError("WAV sub chunk 2 ID not found")
        self.first_sample_offset = 44 + offset

    def play(self, wav_file, loop=False):
        if self.state == Player.PLAY:
            raise ValueError("already playing a WAV file")
        elif self.state == Player.PAUSE:
            raise ValueError("paused while playing a WAV file")
        else:
            self.wav = open(self.root + wav_file, "rb")
            self.loop = loop
            self.parse(self.wav)
            self.audio_out = I2S(
                self.id,
                sck=self.sck_pin,
                ws=self.ws_pin,
                sd=self.sd_pin,
                mode=I2S.TX,
                bits=self.bits_per_sample,
                format=self.format,
                rate=self.sample_rate,
                ibuf=self.ibuf,
            )
            _ = self.wav.seek(self.first_sample_offset)
            self.audio_out.irq(self.i2s_callback)
            self.nflush = self.ibuf // self.sbuf + 1
            self.state = Player.PLAY
            _ = self.audio_out.write(self.silence_samples)

    def resume(self):
        if self.state != Player.PAUSE:
            raise ValueError("can only resume when WAV file is paused")
        else:
            self.state = Player.RESUME

    def pause(self):
        if self.state == Player.PAUSE:
            pass
        elif self.state != Player.PLAY:
            raise ValueError("can only pause when WAV file is playing")
        self.state = Player.PAUSE

    def stop(self):
        self.state = Player.FLUSH

    def isplaying(self):
        if self.state != Player.STOP:
            return True
        else:
            return False

SCK_PIN = 32
WS_PIN = 25
SD_PIN = 33
I2S_ID = 0
BUFFER_LENGTH_IN_BYTES = 40000

Speaker = Player(
    id=I2S_ID,
    sck_pin=Pin(SCK_PIN),
    ws_pin=Pin(WS_PIN),
    sd_pin=Pin(SD_PIN),
    ibuf=BUFFER_LENGTH_IN_BYTES,
)
