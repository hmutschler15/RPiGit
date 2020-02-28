#   Hamilton Mutschler
#   Team 13: T2V
#   ENGR 340 Senior Design
#   Traffic Light Application:
#   Bluetooth Communication Testing

# simple inquiry example
import bluetooth
import re
from time import sleep

# LF Robot BT module address
bdAddr = "FC:58:FA:22:B4:C6"
# create a socket for connection to device
socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# CHANNEL IS 1 TO MATCH BT DEVICE SERVER
channel = 1

# decode utf data
def decode_data(data):
    # decode utf
    decodedData = data.decode('utf-8', 'ignore')
    # decode any regular expression data
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    finalData = ansi_escape.sub('', decodedData)
    return finalData

# receive bt data
def receive(timeout):
    # set timeout to trigger if receive from device takes an abnormally long time
    socket.settimeout(timeout)
    rxData = ''
    # receive from socket
    try:
        rxData = (socket.recv(2048))
    except Exception as e:
        print(e)
        return -1
    # decode utf data
    decodedbdData = decode_data(rxData)
    return decodedbdData

# try to connect to device
try:
    socket.connect((bdAddr, channel))
except Exception:
    print("Connection to bluetooth device failed.")
    quit()       

# # receive connected response
# bdData = ''
# while '\r\n' not in bdData:
#     receivedData = receive(10)
#     if receivedData == -1:
#         break
#     else:
#         bdData += receivedData
#         print(bdData)
# socket.send('$1#')
# # receive command response
# bdData = ''
# while '#' not in bdData:
#     receivedData = receive(5)
#     if receivedData == -1:
#         break
#     else:
#         bdData += receivedData
#         print(bdData)
# sleep(5)
# socket.send('$0#')

while True:
    command = input("Enter '1' to go.\r\nEnter '0' to stop.\r\n")
    if command == '1':
        try:
            socket.send('$1#')
        except Exception as e:
            print("Go command failed to send.")
    else:
        try:
            socket.send('$0#')
        except Exception as e:
            print("Stop command failed to send.")