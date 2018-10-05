#! /usr/bin/python3

from PyCRC.CRC16 import CRC16
from PyCRC.CRC16DNP import CRC16DNP
from PyCRC.CRC16Kermit import CRC16Kermit
from PyCRC.CRC32 import CRC32
from PyCRC.CRCCCITT import CRCCCITT

imgLida = "/home/mateusenrico/Documentos/Insper/CamadaFisica/Projeto 5 - Fragmentacao/img/x.png"
img = open(imgLida,'rb')
txBufferIMG = img.read()
data = txBufferIMG
#data = str(txBufferIMG)
print(CRC16().calculate(data))
