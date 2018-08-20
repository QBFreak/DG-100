#!/usr/bin/env python3

"""
    Put the GlobalSat DG-100 into "GMouse Mode"
    (Begin outputting NEMA sentences)
"""

# START a0 a2 00 02 bc 01 00 bd b0 b3
# STOP  02 00 01 85 84 a0 a2 00 02 bc 00 00 bc b0 b3

import binascii
import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)
ser.write(binascii.unhexlify('a0a20002bc0100bdb0b3'))
ser.close()
