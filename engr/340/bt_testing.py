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


# decode raw utf data received from bt device
def decode_data(data):
    # decode utf
    decodedData = data.decode('utf-8', 'ignore')
    # decode any regular expression data
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    finalData = ansi_escape.sub('', decodedData)
    return finalData

# receive raw bt data
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

# send data to connected bluetooth devices
def send(device, command):
    if device == 1:
        if command == 1:
            try:
                socket1.send('$1#')
            except Exception as e:
                print("Device 1")
                print(e)
        else:
            try:
                socket1.send('$0#')
            except Exception as e:
                print("Device 1")
                print(e)
    elif device == 2:
        if command == 1:
            try:
                socket2.send('$1#')
            except Exception as e:
                print("Device 2")
                print(e)
        else:
            try:
                socket2.send('$0#')
            except Exception as e:
                print("Device 2")
                print(e)

# connect to device
try:
    socket1.connect((bdAddr1, 1))
    print("Device 1 connected successfully.")
    socket2.connect((bdAddr2, 1))
    print("Device 2 connected successfully.")
except Exception as e:
    print(e)
    quit()       
print("Starting control of devices via terminal")
# main loop: control of devices via commandline
while True:
    print("Shared commands: '00' to start and 'Enter' to stop")
    command = input("Command format: (device number)(stop'0'/go'1')\r\n")
    if command == "10":
        try:
            socket1.send('$0#')
        except Exception as e:
            print("Device 1: stop command failed to send")
    elif command == "11":
        try:
            socket1.send('$1#')
        except Exception as e:
            print("Device 1: go command failed to send")
    elif command == "20":
        try:
            socket2.send('$0#')
        except Exception as e:
            print("Device 2: stop command failed to send")
    elif command == "21":
        try:
            socket2.send('$1#')
        except Exception as e:
            print("Device 2: go command failed to send")
    elif command == "00":
        try:
            socket1.send('$1#')
            socket2.send('$1#')
        except Exception as e:
            print("Go all command failed to send.")
    else:
        try:
            socket1.send('$0#')
            socket2.send('$0#')
        except Exception as e:
            print("Stop all command failed to send.")