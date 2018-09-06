
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("comecou")

from enlace import *
import time
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
    imgLida = "/home/mateusenrico/Documentos/Insper/CamadaFisica/Projeto 4 - HandShake/img/vai.png"
    img = open(imgLida,'rb')
    txBufferIMG = img.read()
    txLenIMG    = len(txBufferIMG)
    print("Tempo esperado para conteudo")
    print("{} s".format(txLenIMG*10/com.baudrate))

    flagSyn = False

    while not com.rx.getIsEmpty:
        pass

    rxBuffer, rxTipo = com.rx.getNData()

    if rxTipo == 1:
        print('Chegou 1')
        com.sendData(0,2)
        print('Enviou 2')

    while not com.rx.getIsEmpty:
        pass

    rxBuffer, rxTipo = com.rx.getNData()

    if rxTipo == 3:
        print('Chegou 3')

        print("tentado transmitir .... {} bytes".format(txLenIMG)) ### data

        com.sendData(txBufferIMG,4)
        # Atualiza dados da transmissão
        txSize = com.tx.getStatus()
        print('Enviou 4')

    ack = False
    if ack == False:
        while not com.rx.getIsEmpty:
            pass

        rxBuffer, rxTipo = com.rx.getNData()

        if rxTipo == 5:
            print("Chegou 5, envio foi correto")
            com.sendData(0,7)
            print("Enviou 7")
            ack = True
        elif rxTipo == 6:
            print("Chegou 6, reenviando 4")
            com.sendData(txBufferIMG,4)
            ack = False
        else:
            print("caso estranho")

    if ack == True:
        com.disable()

    # Encerra comunicação
    print("-------------------------")
    print("Comunicação encerrada")
    print("-------------------------")

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()