# screens

from machine import Pin, SPI
from machine import Pin, SoftI2C
from Screen import Screen
from framebuf import FrameBuffer, MONO_HLSB

oled = Screen(addr=0x3d)
oled1 = Screen(addr=0x3c)

with open('/pymadethis.pbm', 'rb') as f:
    f.readline()
    f.readline()
    f.readline()
    data = bytearray(f.read())
fbuf = FrameBuffer(data, 128, 64, MONO_HLSB)

oled.invert(1)
oled.blit(fbuf, 0, 0)
oled.show()

with open('/pymadethis.pbm', 'rb') as f:
    f.readline()
    f.readline()
    f.readline()
    data = bytearray(f.read())
fbuf1 = FrameBuffer(data, 128, 64, MONO_HLSB)

oled1.invert(1)
oled1.blit(fbuf1, 0, 0)
oled1.show()


# potentiometer + servo

from machine import Pin, ADC
from servo import Servo
from time import sleep

x = ADC(Pin(39))
y = ADC(Pin(36))
x.atten(ADC.ATTN_11DB)
y.atten(ADC.ATTN_11DB)

servo_x = Servo(Pin(26))
servo_y = Servo(Pin(14))

while False:
	print("x = ", x.read() / 4096 * 360)
	print("y = ", y.read() / 4096 * 360)
	servo_x.write_angle(int(x.read() / 4096 * 360))
	servo_y.write_angle(int(y.read() / 4096 * 360))
	sleep(0.25)


# webrepl

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

# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

# Attempt to connect to WiFi network
do_connect('your_ssid', 'your_password')

import webrepl
webrepl.start()



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