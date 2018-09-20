
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("comecou")

from enlace import *
import time
import math
from tkinter import filedialog, ttk
from tkinter import *
from tkinter.filedialog import askopenfilename
 
serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
#serialName = "COM4"                  # Windows(variacao de)


def main():
    # Inicializa enlace ... variavel com possui todos os metodos e propriedades do enlace, que funciona em threading
    com = enlace(serialName)

    # Ativa comunicacao
    com.enable()

    #verificar que a comunicação foi aberta
    print("comunicação aberta")

    #Gerando dados
    print ("gerando dados para transmissao :")
  
    print("Carregando imagem")
    # Lendo a imagem
    def OpenFile():
        name = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                            filetypes =(("PNG Files", "*.png"),("All Files","*.*")),
                            title = "Choose a file."
                            )
        print (name)
    
    #Using try in case user types in unknown file or closes without choosing a file.
        return name 
    #imgLida = OpenFile() 
    #imgLida = "/home/mateusenrico/Documentos/Insper/CamadaFisica/Projeto 5 - Fragmentacao/img/x.png"
    #imgLida = imgEscrita = "/home/vitorsv/Dropbox/Insper/2018.2/Camada Física/CamadaFisica/Projeto 5 - Fragmentacao/img/vai.png"
    imgLida = imgEscrita = "/home/vitorsv/Dropbox/Insper/2018.2/Camada Física/CamadaFisica/Projeto 5 - Fragmentacao/img/x.png"
    img = open(imgLida,'rb')
    txBufferIMG = img.read()
    txLenIMG    = len(txBufferIMG)
    print("-------------------------")
    print("Tempo esperado para conteudo")
    print("{} s".format(txLenIMG*10/com.baudrate))

    while not com.rx.getIsEmpty:
        pass

    rxBuffer, rxTipo, rxErro, rxPacote, maxPacotes = com.rx.getNData()
    print("Vendo se chegou 1")
    if rxTipo == 1:
        print("-------------------------")
        print('Chegou 1')
        time.sleep(1)
        com.sendData(0,2)
        print("-------------------------")
        print('Enviou 2')

    com.rx.clearBuffer()

    inicio = time.time()
    timeout = 0
    while com.rx.getIsEmpty():
        timeout = time.time() - inicio
        if timeout >= 5:
            com.sendData(0,2)
            inicio = time.time()
        estado = com.rx.getIsEmpty()

    rxBuffer, rxTipo, rxErro, rxPacote, maxPacotes = com.rx.getNData()

    if rxTipo == 3:
        print("-------------------------")
        print('Chegou 3')
        print("-------------------------")
        print("tentado transmitir .... {} bytes".format(txLenIMG)) ### data

        sizeInteiro = len(txBufferIMG)
        maxSize = 255
        number = math.ceil(sizeInteiro/maxSize)

        i = 0
        while i < number:
            time.sleep(1)
            com.sendData(txBufferIMG,4,i)
            # Atualiza dados da transmssão
            txSize = com.tx.getStatus()
            print("-------------------------")
            print('Enviou 4, pacote {}'.format(i))
            ack = False
            if ack == False:
                inicio = time.time()
                timeout = 0
                while com.rx.getIsEmpty():
                    timeout = time.time() - inicio
                    if timeout >= 5:
                        time.sleep(1)
                        com.sendData(txBufferIMG,4,i)
                        inicio = time.time()
                    estado = com.rx.getIsEmpty()

                rxBuffer, rxTipo, rxErro, rxPacote, maxPacotes = com.rx.getNData()

            if rxTipo == 5:
                print("-------------------------")
                print("Chegou 5, mais um envio foi correto")
                time.sleep(1)
                i += 1
                pass
                #ack = True
            elif rxTipo == 6:
                print("-------------------------")
                print("Chegou 6, reenviando 4, pacote {}".format(i))
                time.sleep(1)
                pass
                #ack = False
            elif rxTipo == 8:
                print("-------------------------")
                print("Chegou 8, reenviando 4, pacote {}".format(i))
                time.sleep(1)
                pass
            else:
                print("-------------------------")
                print("Caso estranho")
                break


    time.sleep(3)
    com.sendData(0,7)
    print("-------------------------")
    print("Enviou 7")

    com.disable()

    # Encerra comunicação
    print("-------------------------")
    print("Comunicação encerrada")
    print("-------------------------")

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()