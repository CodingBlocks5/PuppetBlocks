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


# --- Second stage: update libraries
import upip

upip.install('webrepl')
upip.install('shutil')
upip.install('urequests')


# --- Third stage: update time from the internet
import ntptime

ntptime.settime()


# --- Fourth stage: activate webrepl
import webrepl

webrepl.start()
