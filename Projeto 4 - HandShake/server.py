
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Física da Computação
#Carareto
#17/02/2018
#  Aplicação
####################################################

print("comecou")

#aokdaopskdp

from enlace import *
import time
from tkinter import filedialog, ttk
from tkinter import *
from tkinter.filedialog import askopenfilename
 
# voce deverá descomentar e configurar a porta com através da qual ira fazer a
# comunicaçao
# Serial Com Port
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
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
    imgLida = OpenFile() 

    img = open(imgLida,'rb')
    txBuffer = img.read()
    txLen    = len(txBuffer)
    print("Tempo esperado")
    print("{} s".format(txLen*10/com.baudrate))

    flagSyn = False

    while not com.rx.getIsEmpty:
        pass

    rxBuffer, rxTipo = com.rx.getNData()
    print('Chegou 1')

    if rxTipo == 1:
        com.sendData(0,2)
        print('enviou 2')

    # Transmite dado
    #print("tentado transmitir .... {} bytes".format(txLen)) ### data

    #com.sendData(txBuffer,4)
    # Atualiza dados da transmissão
    #txSize = com.tx.getStatus()

    # Encerra comunicação
    print("-------------------------")
    print("Comunicação encerrada")
    print("-------------------------")
    com.disable()

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()