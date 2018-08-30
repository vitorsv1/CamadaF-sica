
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Física da Computação
#Carareto
#17/02/2018
#  Aplicação
####################################################

print("comecou")

#agora aqui

from enlace import *
import time

# voce deverá descomentar e configurar a porta com através da qual ira fazer a
# comunicaçao
# Serial Com Port
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
#serialName = "COM7"                  # Windows(variacao de)

print("porta COM aberta com sucesso")

def main():
    # Inicializa enlace ... variavel com possui todos os metodos e propriedades do enlace, que funciona em threading
    com = enlace(serialName)

    # Ativa comunicacao
    com.enable()

    #verificar que a comunicação foi aberta
    print("comunicação aberta")

    #imgEscrita = "C:/Users/Mateus Enrico/Documents/Insper/CamadaFisica/Projeto 3/img/recebido.png"
    #imgEscrita = "C:/Users/vitor/Dropbox/Insper/2018.2/Camada Física/CamadaFisica/Projeto 3/img/recebido.png"
    imgEscrita = "/home/vitorsv/Dropbox/Insper/2018.2/Camada Física/CamadaFisica/Projeto 4 - HandShake/img/recebido.png"
    # a seguir ha um exemplo de dados sendo carregado para transmissao
    # voce pode criar o seu carregando os dados de uma imagem. Tente descobrir
    #como fazer isso

    # SYNC
    #flagSyn = False
    #respSyn = False
    print("Sync")

    com.sendData(0,1)

    while not com.rx.getIsEmpty:
        pass

    rxBuffer, rxTipo = com.rx.getNData()

    if rxTipo == 2:
        print("Chegou 2")
        com.sendData(0,3)
        print("Enviou 3")

    #while not flagSyn:
    #    while not respSyn:
    #        com.sendData(0,1)
    #       inicio = time.time()
    #       fim = time.time()
    #        medido = fim - inicio
    #        while not com.rx.getIsEmpty():
    #            fim = time.time()
    #            medido = fim - inicio
    #            if medido > 5:
    #                break
    #        if medido < 5:
    #            respSyn = True
    #            print("flag 1 foi")
    #    rxBuffer, rxTipo = com.rx.getNData()

     #   if rxTipo == 2:
     #       flagSyn = True
    
    #com.sendData(0,3)
    
    #while not flagDatazsdtbgasertbd

    # Faz a recepção dos dados
    print ("Recebendo dados .... ")
    
    while not com.rx.getIsEmpty:
        pass
        
    #rxBuffer, rxTipo = com.rx.getNData()
    
    
    # Criando imagem nova
    print ("Testando rxbuffer...")
    #print (rxBuffer)
    imgNova = open(imgEscrita,'wb')
    imgNova.write(rxBuffer)
    imgNova.close()

    # Encerra comunicação
    print("-------------------------")
    print("Comunicação encerrada")
    print("-------------------------")
    com.disable()

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()