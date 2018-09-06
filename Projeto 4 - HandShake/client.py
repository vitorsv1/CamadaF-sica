
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("comecou")

from enlace import *
import time

serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
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
    #imgEscrita = "/home/vitorsv/Dropbox/Insper/2018.2/Camada Física/CamadaFisica/Projeto 4 - HandShake/img/recebido.png"
    imgEscrita = "/home/mateusenrico/Documentos/Insper/CamadaFisica/Projeto 4 - HandShake/img/recebido.png"


    # SYNC
    print("Sync")

    com.sendData(0,1)

    while not com.rx.getIsEmpty:
        pass

    rxBuffer, rxTipo = com.rx.getNData()

    if rxTipo == 2:
        print("Chegou 2")
        com.sendData(0,3)
        print("Enviou 3")

    while not com.rx.getIsEmpty:
        pass

    rxBuffer, rxTipo = com.rx.getNData()

    if rxTipo == 4:
        print("Chegou 4")
        
        imgNova = open(imgEscrita,'wb')
        imgNova.write(rxBuffer)
        imgNova.close()
        
        com.sendData(0,5)
        print("Enviou 5")

    while not com.rx.getIsEmpty:
        pass

    rxBuffer, rxTipo = com.rx.getNData()

    if rxTipo == 7:
        print("Chegou 7")
        com.disable()

    # Encerra comunicação
    print("-------------------------")
    print("Comunicação encerrada")
    print("-------------------------")

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()