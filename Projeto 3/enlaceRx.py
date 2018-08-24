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
#        temPraLer = self.getBufferLen()
#        print('leu %s ' + str(temPraLer) )
        
        #if self.getBufferLen() < size:
            #print("ERROS!!! TERIA DE LER %s E LEU APENAS %s", (size,temPraLer))
        size = 0

        while ((self.getBufferLen() > size) or (self.getBufferLen()==0)):
            size = self.getBufferLen()
            time.sleep(0.3)
            print("Recebendo...")
        return(self.getBuffer(size))


    def clearBuffer(self):
        """ Clear the reception buffer
        """
        self.buffer = b""

    #----------------Metodos-Novos----------------#
    def desempacota(self,dado):
        # Info
        headSize = 5
        eopSize = 4
    
        # Info de EOP
        confirmaEop = [255, 254, 253, 252]
    
        count = 0
        head = bytearray()
        pay = bytearray()
        eop = bytearray()
    
        for i in dado:
            if count < headSize:
                #print(i)
                if count == 0:
                    head.extend(i.to_bytes(1,'big'))
                else:
                    head.extend(i.to_bytes(2,'big'))
                count += 1
        tamanho = head[0]
        pacote = head[1] * 256 + head[2]
        maxPacotes = head[3] * 256 + head[4]
        #print(head)
        
        count = 1
        point = 0
        flagEop = 0
        correto = False
        corretoEop = False
        corretoPay = False

        for i in range(len(dado)):
            if i + 3 < len(dado):
                if dado[i] == 255 and dado[i+1] == 254 and dado[i+2] == 253 and dado[i+3] == 252:
                    corretoEop = True
                    flagEop = i
                    break

        if (flagEop - headSize) == tamanho:
            corretoPay = True
        
        if corretoPay & corretoEop:
            correto = True

        if correto:
            print("envio correto")
            return pay
        else:
            if not corretoPay:
                print("erro no tamanho do payload")
            else:
                print("erro no EOP")
            return -1




