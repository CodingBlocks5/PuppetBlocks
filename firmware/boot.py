#
#   @file : boot.py
#   @authors : PuppetBlocks team
#   @date : 22 February 2023
#

# --- First stage: connect to network
import network
import Secrets

sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect(Secrets.NETWORK_ID, Secrets.NETWORK_PASSWORD)
    while not sta_if.isconnected():
        pass
print('Network configuration:', sta_if.ifconfig())


# --- Second stage: connect to SD card
import machine
import os

sd = machine.SDCard(
    slot=2,
    width=1,
    cd=None,
    wp=None,
    sck=machine.Pin(18),
    miso=machine.Pin(19),
    mosi=machine.Pin(23),
    cs=machine.Pin(5),
    freq=20000000
)
os.mount(sd, "/sd")
print('SD mounting has completed!')


# --- Third stage: update libraries
import upip

upip.install('webrepl')
upip.install('shutil')
upip.install('urequests')


# --- Fourth stage: update time from the internet
import ntptime

ntptime.settime()


# --- Fifth stage: activate webrepl
import webrepl

webrepl.start()
