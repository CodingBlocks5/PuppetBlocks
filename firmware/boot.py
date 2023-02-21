# ---boot:

def do_connect(ssid, pwd):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, pwd)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect('your_ssid', 'your_password')

import webrepl
webrepl.start()

from machine import Pin, SPI
import machine, os
sd = machine.SDCard(slot=2, width=1, cd=None, wp=None, sck=Pin(18), miso=Pin(19), mosi=Pin(23), cs=Pin(5), freq=20000000)
os.mount(sd, "/sd")

# ---


# time

from machine import RTC
import ntptime
import time

rtc = RTC()
ntptime.settime()
(year, month, day, weekday, hours, minutes, seconds, subseconds) = rtc.datetime()
print ("UTC Time: ")
print((year, month, day, hours, minutes, seconds))

sec = ntptime.time()
timezone_hour = 5.50
timezone_sec = timezone_hour * 3600
sec = int(sec + timezone_sec)
(year, month, day, hours, minutes, seconds, weekday, yearday) = time.localtime(sec)
print ("IST Time: ")
print((year, month, day, hours, minutes, seconds))
rtc.datetime((year, month, day, 0, hours, minutes, seconds, 0))
disconnect()

# file download

import shutil
import urequests
import os
import time
import machine
from machine import Pin, SPI, SPI, SDCard
from wavplayer import WavPlayer

sd = machine.SDCard(slot=2, width=1, cd=None, wp=None, sck=Pin(18), miso=Pin(19), mosi=Pin(23), cs=Pin(5), freq=20000000)
os.mount(sd, "/sd")

url = 'https://firebasestorage.googleapis.com/v0/b/puppetblocks.appspot.com/o/music-16k-32bits-mono.wav?alt=media&token=93f5266b-e6c0-498f-a6a9-0f1e892d4df3'
local_filename = url.split('?')[0].split('/')[-1]
r = urequests.get(url, stream=True)
if r.status_code == 200:
    with open('/sd/PB/{}'.format(local_filename), 'wb') as f:
        shutil.copyfileobj(r.raw, f)
print('The file has downloaded!')

SCK_PIN = 32
WS_PIN = 25
SD_PIN = 33
I2S_ID = 0
BUFFER_LENGTH_IN_BYTES = 40000

wp = WavPlayer(
    id=I2S_ID,
    sck_pin=Pin(SCK_PIN),
    ws_pin=Pin(WS_PIN),
    sd_pin=Pin(SD_PIN),
    ibuf=BUFFER_LENGTH_IN_BYTES,
)

wp.play(local_filename , loop=False)
time.sleep(10)
wp.pause()
time.sleep(5)
wp.resume()
