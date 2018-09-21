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
from PyCRC.CRC16 import CRC16

# Threads
import threading

# Class
class RX(object):
    """ This class implements methods to handle the reception
        data over the p2p fox protocol
    """
    
    def __init__(self, fisica):
        """ Initializes the TX class
        """
        self.fisica      = fisica
        self.buffer      = bytes(bytearray())
        self.threadStop  = False
        self.threadMutex = True
        self.READLEN     = 1024
        self.timeout     = 0

    def thread(self): 
        """ RX thread, to send data in parallel with the code
        essa é a funcao executada quando o thread é chamado. 
        """
        while not self.threadStop:
            if(self.threadMutex == True):
                rxTemp, nRx = self.fisica.read(self.READLEN)
                if (nRx > 0):
                    self.buffer += rxTemp
                time.sleep(0.01)

    def threadStart(self):
        """ Starts RX thread (generate and run)
        """
        self.thread = threading.Thread(target=self.thread, args=())
        self.thread.start()

    def threadKill(self):
        """ Kill RX thread
        """
        self.threadStop = True

    def threadPause(self):
        """ Stops the RX thread to run

        This must be used when manipulating the Rx buffer
        """
        self.threadMutex = False

    def threadResume(self):
        """ Resume the RX thread (after suspended)
        """
        self.threadMutex = True

    def getIsEmpty(self):
        """ Return if the reception buffer is empty
        """
        if(self.getBufferLen() == 0):
            return(True)
        else:
            return(False)

    def getBufferLen(self):
        """ Return the total number of bytes in the reception buffer
        """
        return(len(self.buffer))

    def getAllBuffer(self, len):
        """ Read ALL reception buffer and clears it
        """
        self.threadPause()
        b = self.buffer[:]
        self.clearBuffer()
        self.threadResume()
        return(b)

    def getBuffer(self, nData):
        """ Remove n data from buffer
        """
        self.threadPause()
        b           = self.buffer[0:nData]
        self.buffer = self.buffer[nData:]
        self.threadResume()
        return(b)

    def getNData(self):
        """ Read N bytes of data from the reception buffer

        This function blocks until the number of bytes is received
        """
        
        #if self.getBufferLen() < size:
            #print("ERROS!!! TERIA DE LER %s E LEU APENAS %s", (size,temPraLer))
        size = 0
        #inicio = time.time()
        while ((self.getBufferLen() > size) or (self.getBufferLen()==0)):
            size = self.getBufferLen()
            time.sleep(0.3) # DIFF
            print("recebendo...") #DIFF
        #self.timeout = time.time() - inicio
        dados = self.getBuffer(size) # DIFF
        #print(dados)
        data,tipo,erro,pacote,maximo = self.desempacota(dados)
        return(data,tipo,erro,pacote,maximo)# DIFF


    def clearBuffer(self):
        """ Clear the reception buffer
        """
        self.buffer = b""

    #----------------Metodos-Novos----------------#
    def desempacota(self,dado):
        # Info
        headSize = 6
        headType = 6
        count = 0
        head = bytearray()
        pay = bytearray()
        eop = bytearray()
        
    
        for i in dado:
            if count < headType:
                #print(i)
                if count == 6:
                    head.extend(i.to_bytes(1,'big'))
                else:
                    head.extend(i.to_bytes(1,'big'))
                count += 1
        tamanho = head[0]
        tipo = head[1]
        #MUDAR OS VALORES QUE MULTIPLICAM O PACOTE E MAXPACOTE
        pacote = head[2]
        maxPacotes = head[3]
        print("head {}".format(head))
        

        count = 1
        flagEop = 0
        correto = False
        corretoEop = False
        corretoPay = False
        flagStuff = []
        stuff = False

        for i in range(len(dado)):
            if i + 3 < len(dado):
                #MUDAR OS VALORES DOS IFs PARA OS LIDOS NO HEAD COM O TAMANHO DO PAYLOAD, PAYLOAD -1 ...
                if dado[i] == 255 and dado[i+1] == 254 and dado[i+2] == 253 and dado[i+3] == 252: #0xFF 0xFE 0xFD 0xFC
                    if i - 2 > 0:
                        #PROVAVELMENTE MUDE AQUI TBM COM A MUDANÇA DO PAYLOAD
                        if dado[i-2] == 221 and dado[i-1] == 238: #2 bytes, 0xDD e 0xEE
                            stuff = True
                            flagStuff.append(i-2)
                        else:
                            corretoEop = True
                            flagEop = i
                            #print("INTERNO FLAG: {}".format(flagEop))
                            break

        dadoFiltro = bytearray()

        count = 0
        corretoStuff = False

        if stuff:
            for i in flagStuff:
                dadoFiltro = dado[:i-2*count] + dado[(i+2)-2*count:]
                count += 1
        else:
            dadoFiltro = dado
        flagEop -= count * 2


        pay = dadoFiltro[headSize:flagEop]
        print(pay)
        corretoCRC = False
        crc=CRC16().calculate(pay)
        print("&&&&&&&&&&&&")
        print(crc)
        crc_veio = int.from_bytes(head[4:6],byteorder='big')
        #CRCZAO = head[4] << 8 + head[5]
        print(crc_veio)
        if crc == crc_veio:
            corretoCRC = True
        
        if count == len(flagStuff):
            corretoStuff = True

        print ("Subtracao {}".format(flagEop-headSize))
        print("Tamanho {}".format(tamanho))
        if (flagEop - headSize) == tamanho:
            corretoPay = True

        if corretoPay and corretoEop and corretoStuff and corretoCRC:
            correto = True

        if correto:
            #print("envio correto")
            erro = 0
            return pay,tipo,erro,pacote,maxPacotes
        else:
            if not corretoPay:
                #print("erro no tamanho do payload")
                erro = 1
                return -1,tipo,erro,pacote,maxPacotes
            elif not corretoEop:
                #print("erro no EOP")
                erro = 2
                return -1,tipo,erro,pacote,maxPacotes
            elif not corretoStuff:
                #print("erro na remocao do stuff")
                erro = 3
                return -1,tipo,erro,pacote,maxPacotes
            elif not corretoCRC:
                erro = 4
                return -1,tipo,erro,pacote,maxPacotes