#!/usr/bin./python

import sys
import time
import difflib
import pigpio
import xbee

RxGpioPin = 18
baudRate = 9600
numBit = 8

XB = xbee.XBEE('/dev/serial0',baudRate,1)

try:
    pi = pigpio.pi()
    pi.set_mode(RxGpioPin, pigpio.INPUT)
    pi.bb_serial_read_open(RxGpioPin, baudRate, numBit)
    
    while 1:
        (count,data) = pi.bb_serial_read(RxGpioPin)
        if count:
            data = data.decode()
            
            startIndex = 0
            endIndex = len(data)
            # find index of $GPGGA within GPSIn (-1 means it's not # in GPSIn)
            dataIndex = data.find("$GPGGA", startIndex, endIndex)
            if dataIndex == -1:
                continue
            else:        
                # find index end of line
                dataLineEnd = data.find('\r', dataIndex, endIndex)
                GPSLine = data[dataIndex:dataLineEnd]
            
                numCommas = 0
                i = 7
                while i < len(GPSLine):
                    if GPSLine[i] == ',':
                        numCommas += 1
                    else:
                        if numCommas == 0:
                            GPSTime += GPSLine[i]
                        elif numCommas == 1:
                            GPSLat += GPSLine[i]
                        elif numCommas == 2:
                            GPSDirNS += GPSLine[i]
                        elif numCommas == 3:
                            GPSLong += GPSLine[i]
                        elif numCommas == 4:
                            GPSDirEW += GPSLine[i]
                    i += 1
                    
                XB.sendData(GPSLine)
                    
        time.sleep(1)

except:
    print("error")
    pi.bb_serial_read_close(RxGpioPin)
    pi.stop()
