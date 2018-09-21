#! /usr/bin/python3

from PyCRC.CRC16 import CRC16
from PyCRC.CRC16DNP import CRC16DNP
from PyCRC.CRC16Kermit import CRC16Kermit
from PyCRC.CRC32 import CRC32
from PyCRC.CRCCCITT import CRCCCITT

data = '0xF3'
dado = '123'
print(CRC16().calculate(data))