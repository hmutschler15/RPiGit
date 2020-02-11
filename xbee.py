#!/usr/bin/env python
import time
import serial

class XBEE:
    def __init__(self, port, baudRate, timeout):
        self.port = port
        self.baudRate = baudRate
        self.timeout = timeout
        self.ser = serial.Serial(
            port=self.port,
            baudrate = self.baudRate,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=self.timeout             
         )

    def readData(self):
        return self.ser.readline().strip()
        
    def sendData(self, data):
        self.ser.write(str.encode(data))
