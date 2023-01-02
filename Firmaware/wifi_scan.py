#
# DELETE ENVIROMENT
#
import sys
sys.exit()

#
# BASED ON: https://wokwi.com/projects/305570169692881473
#
import network

print("Scanning for WiFi networks, please wait...")
print("")

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

authmodes = ['Open', 'WEP', 'WPA-PSK' 'WPA2-PSK4', 'WPA/WPA2-PSK']
for (ssid, bssid, channel, RSSI, authmode, hidden) in sta_if.scan():
  print("* {:s}".format(ssid))
  print("   - Auth: {} {}".format(authmodes[authmode] if authmode < len(authmodes) else 'UNKNOWN', '(hidden)' if hidden else ''))
  print("   - Channel: {}".format(channel))
  print("   - RSSI: {}".format(RSSI))
  print("   - BSSID: {:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}".format(*bssid))
  print()
 