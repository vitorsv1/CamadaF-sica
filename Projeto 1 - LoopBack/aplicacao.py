
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Física da Computação
#Carareto
#17/02/2018
#  Aplicação
####################################################

print("comecou")

from enlace import *
import time

# voce deverá descomentar e configurar a porta com através da qual ira fazer a
# comunicaçao
# Serial Com Port
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

#serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
serialName = "COM3"                  # Windows(variacao de)

print("porta COM aberta com sucesso")

def main():
    # Inicializa enlace ... variavel com possui todos os metodos e propriedades do enlace, que funciona em threading
    com = enlace(serialName)

    # Ativa comunicacao
    com.enable()

    #verificar que a comunicação foi aberta
    print("comunicação aberta")

    imgLida = "C:/Users/Mateus Enrico/Documents/Insper/CamadaFisica/Projeto 3/img/vai.png"

    imgEscrita = "C:/Users/Mateus Enrico/Documents/Insper/CamadaFisica/Projeto 3/img/recebido.png"

    # a seguir ha um exemplo de dados sendo carregado para transmissao
    # voce pode criar o seu carregando os dados de uma imagem. Tente descobrir
    #como fazer isso
    print ("gerando dados para transmissao :")
  
    print("Carregando imagem")
    # Lendo a imagem
    img = open(imgLida,'rb')
    txBuffer = img.read()
    txLen    = len(txBuffer)
    print(txLen)

    #ListTxBuffer =list()
    #for x in range(0,20):
    #   ListTxBuffer.append(x)
    #txBuffer = bytes(ListTxBuffer)
    #txLen    = len(txBuffer)
    #print(txLen)


    # Transmite dado
    print("tentado transmitir .... {} bytes".format(txLen))
    com.sendData(txBuffer)

    #Continua quando a transmissão acabar
    while(com.tx.getIsBussy()):
        pass

    # Atualiza dados da transmissão
    txSize = com.tx.getStatus()
    print("Tamanho de {}".format(txSize))

    # Faz a recepção dos dados
    print ("Recebendo dados .... ")
    bytesSeremLidos=com.rx.getBufferLen()
    
    # Recebe dados
    rxBuffer, nRx = com.getData(txLen)

    # log
    print ("Lido              {} bytes ".format(nRx))
    
    # Criando imagem nova
    print ("Criando nova imagem...")
    imgNova = open(imgEscrita,'wb')
    imgNova.write(rxBuffer)
    imgNova.close()
    print (rxBuffer)

    # Encerra comunicação
    print("-------------------------")
    print("Comunicação encerrada")
    print("-------------------------")
    com.disable()

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
