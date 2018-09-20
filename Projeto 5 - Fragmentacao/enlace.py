#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Física da Computação
#Carareto
#17/02/2018
#  Camada de Enlace
####################################################

# Importa pacote de tempo
import time

# Construct Struct
#from construct import *

# Interface Física
from interfaceFisica import fisica

# enlace Tx e Rx
from enlaceRx import RX
from enlaceTx import TX

class enlace(object):
    """ This class implements methods to the interface between Enlace and Application
    """

    def __init__(self, name):
        """ Initializes the enlace class
        """
        self.fisica      = fisica(name)
        self.rx          = RX(self.fisica)
        self.tx          = TX(self.fisica)
        self.connected   = False
        self.baudrate    = self.fisica.baudrate

    def enable(self):
        """ Enable reception and transmission
        """
        self.fisica.open()
        self.rx.threadStart()
        self.tx.threadStart()

    def disable(self):
        """ Disable reception and transmission
        """
        self.rx.threadKill()
        self.tx.threadKill()
        time.sleep(1)
        self.fisica.close()

    ################################
    # Application  interface       #
    ################################
    def sendData(self, data,tipo,atual=0):
        """ Send data over the enlace interface
        """
        pacote,quantidade,len_pays = self.tx.empacota(data,tipo)
        quantidade -= 1
        print("PACOTE QUE CHEGOU DO EMPACOTA")
        print(pacote)
        print("######################################")
        print("VALOR DO ATUAL É {}".format(atual))
        print("QUANTIDADE: {}".format(quantidade))
        if tipo == 4:
            if atual == 0:
                print('entrou 0')
                mensagem = pacote[:(10+len_pays[atual])]
            elif atual == quantidade:
                print('entrou quantidade')
                mensagem = pacote[(10+len_pays[atual-1])+1:]
            else:
                print('entrou resto')
                mensagem = pacote[(10+len_pays[atual-1])+1:(10+len_pays[atual])]
        else:
            mensagem = pacote

        self.tx.sendBuffer(mensagem)
        time.sleep(1)
        throughput = len(pacote)/self.fisica.tempo
        print("Mensagem a ser enviada")
        print(mensagem)
        print("Throughput: {} kB/s".format(throughput/1024))

    def getData(self, size):
        """ Get n data over the enlace interface
        Return the byte array and the size of the buffer
        """
        print('entrou na leitura e tentara ler ' + str(size) )
        data = self.rx.getNData(size)
        #dados = self.rx.desempacota(data)
        return(data, len(data))
    
