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

import shutil
import urequests
import os
import time
import machine
from machine import Pin, SPI, SPI, SDCard
from wavplayer import WavPlayer

sd = machine.SDCard(slot=2, width=1, cd=None, wp=None, sck=Pin(18), miso=Pin(19), mosi=Pin(23), cs=Pin(5), freq=20000000)
os.mount(sd, "/sd")
