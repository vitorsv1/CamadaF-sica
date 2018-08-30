#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Física da Computação
#Carareto
#17/02/2018
#  Camada de Enlace
####################################################

# Importa pacote de tempo e math
import time
import math

# Threads
import threading

# Class
class TX(object):
    """ This class implements methods to handle the transmission
        data over the p2p fox protocol
    """

    def __init__(self, fisica):
        """ Initializes the TX class
        """
        self.fisica      = fisica
        self.buffer      = bytes(bytearray())
        self.transLen    = 0
        self.empty       = True
        self.threadMutex = False
        self.threadStop  = False

    def thread(self):
        """ TX thread, to send data in parallel with the code
        """
        while not self.threadStop:
            if(self.threadMutex):
                self.transLen    = self.fisica.write(self.buffer)
                #print("O tamanho transmitido. IMpressao dentro do thread {}" .format(self.transLen))
                self.threadMutex = False

    def threadStart(self):
        """ Starts TX thread (generate and run)
        """
        self.thread = threading.Thread(target=self.thread, args=())
        self.thread.start()

    def threadKill(self):
        """ Kill TX thread
        """
        self.threadStop = True

    def threadPause(self):
        """ Stops the TX thread to run

        This must be used when manipulating the tx buffer
        """
        self.threadMutex = False

    def threadResume(self):
        """ Resume the TX thread (after suspended)
        """
        self.threadMutex = True

    def sendBuffer(self, data):
        """ Write a new data to the transmission buffer.
            This function is non blocked.

        This function must be called only after the end
        of transmission, this erase all content of the buffer
        in order to save the new value.
        """
        self.transLen   = 0
        self.buffer = data
        self.threadMutex  = True

    def getBufferLen(self):
        """ Return the total size of bytes in the TX buffer
        """
        return(len(self.buffer))

    def getStatus(self):
        """ Return the last transmission size
        """
        #print("O tamanho transmitido. Impressao fora do thread {}" .format(self.transLen))
        return(self.transLen)
        
    def getIsBussy(self):
        """ Return true if a transmission is ongoing
        """
        return(self.threadMutex)

#----------------Metodos-Novos----------------#
    # ERRO NESSA FUNÇÃO POIS A IMAGEM NÃO FORMA ADEQUADAMENTE
    def empacota(self,dado,tipo):
        tipoEncode = "utf-8"
    
        number = math.ceil(sizeInteiro/maxSize)
        count = number
        envio = bytearray()
    
        while count != 0:
            msg = bytearray()
            head = bytearray()
            pay = bytearray()
            eop = bytearray()

            atual = number - count

            # PAYLOAD
            if tipo == 4:
                sizeInteiro = len(dado)
                maxSize = 255 # 16 bits pra representar o tamanho do payload
                if sizeInteiro <= maxSize:
                    size = sizeInteiro
                    carga = dado[0:]
                else:
                    if count == 1:
                        size = sizeInteiro - (number - 1)*maxSize
                        carga = dado[(maxSize*atual+1):]
                    else:
                        if atual == 0:
                            adendo = 0
                        else:
                            adendo = 1

                        size = maxSize
                        carga = dado[(maxSize*atual+adendo):(maxSize*(atual+1))]
                    
                flagStuff = []
                stuff = False

                for i in range(len(dado)):
                    if i + 3 < len(dado):
                        if dado[i] == 255 and dado[i+1] == 254 and dado[i+2] == 253 and dado[i+3] == 252: #0xFF 0xFE 0xFD 0xFC
                            flagStuff.append(i)
                            stuff = True
                
                cargaFiltro = bytearray()
                contador = 0
                primeiroStuff = 221
                segundoStuff = 238
                if stuff: 
                    for i in flagStuff:
                        cargaFiltro = carga[:i-2*contador]
                        cargaFiltro.extend(primeiroStuff.to_bytes(1,'big'))
                        cargaFiltro.extend(segundoStuff.to_bytes(1,'big'))
                        cargaFiltro += carga[i-2*contador:]
                        contador += 1
                else:
                    cargaFiltro = carga

                pay.extend(bytes(cargaFiltro))
            
            else:
                pay.extend(dado.to_bytes(1,'big'))
            # HEAD
            #So foi dado extend

            # EOP
            primeiro = 255
            segundo = 254
            terceiro = 253
            quarto = 252

            # MONTANDO #
            head.extend(size.to_bytes(1,'big')) 
            head.extend(tipo.to_bytes(1,'big'))
            head.extend(atual.to_bytes(2,'big'))
            head.extend((number-1).to_bytes(2,'big'))

            eop.extend(primeiro.to_bytes(1,'big'))
            eop.extend(segundo.to_bytes(1,'big'))
            eop.extend(terceiro.to_bytes(1,'big'))
            eop.extend(quarto.to_bytes(1,'big'))

            msg.extend(head)
            msg.extend(pay)
            msg.extend(eop)
            # ADICIONA A VARIAVEL PARA O BUFFER
            envio.extend(msg)
            
            count = count - 1
            #print(count)

        overhead = (6 + maxSize + 4) / maxSize
        print("Overhead: {}%".format(overhead*100))

        return(envio)