# Bluetooth Testing

# simple inquiry example
import bluetooth
import re

bdAddr = "FC:58:FA:22:B4:C6"

# nearby_devices = bluetooth.discover_devices(lookup_names=True)
# print("Found {} devices.".format(len(nearby_devices)))

# for addr, name in nearby_devices:
#     print("  {} - {}".format(addr, name))

# create a socket for connection to device
socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# socket.settimeout(10)
# CHANNEL IS 1 TO MATCH BT DEVICE SERVER
channel = 1
# try to connect to device
socket.connect((bdAddr, channel))
print("Connection succeeded.")
socket.send('AT+ADDR?\r\n')
socket.settimeout(5)
bdData = ''
bdData = (socket.recv(2048))
# decode utf
decodedData = bdData.decode('utf-8', 'ignore')
# decode any regular expression data
ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
finalData = ansi_escape.sub('', decodedData)
print(finalData)