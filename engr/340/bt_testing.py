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
bdAddr1 = "FC:58:FA:22:CA:65"
bdAddr2 = "FC:58:FA:22:BC:A6"
# create a socket for connection to device
socket1 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
socket2 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)


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
    socket1.connect((bdAddr1, 1))
    socket2.connect((bdAddr2, 1))
except Exception as e:
    print(e)
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
            socket1.send('$1#')
            socket2.send('$1#')
        except Exception as e:
            print("Go command failed to send.")
    else:
        try:
            socket1.send('$0#')
            socket2.send('$0#')
        except Exception as e:
            print("Stop command failed to send.")