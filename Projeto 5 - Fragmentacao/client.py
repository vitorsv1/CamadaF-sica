
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("comecou")

from enlace import *
import time

serialName = "/dev/ttyACM1"           # Ubuntu (variacao de)
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
    imgEscrita = "/home/vitorsv/Dropbox/Insper/2018.2/Camada Física/CamadaFisica/Projeto 5 - Fragmentacao/img/recebido.png"
    #imgEscrita = "/home/mateusenrico/Documentos/Insper/CamadaFisica/Projeto 5 - Fragmentacao/img/recebido.png"

    print("-------------------------")
    # SYNC
    print("Sync")

    time.sleep(1)
    com.sendData(0,1)

    com.rx.clearBuffer()

    inicio = time.time()
    timeout = 0
    estado = com.rx.getIsEmpty()
    while com.rx.getIsEmpty():
        timeout = time.time() - inicio
        if timeout >= 5:
            com.sendData(0,1)
            inicio = time.time()
        estado = com.rx.getIsEmpty()

    rxBuffer, rxTipo, rxErro, rxPacote, maxPacotes = com.rx.getNData()

    if rxTipo == 2:
        print("-------------------------")
        print("Chegou 2")
        time.sleep(1)
        com.sendData(0,3)
        print("-------------------------")
        print("Enviou 3")

    flagPay = False
    pontos = 0
    while not flagPay:
        com.rx.clearBuffer()

        inicio = time.time()
        timeout = 0
        while com.rx.getIsEmpty():
            timeout = time.time() - inicio
            if timeout >= 5:
                com.sendData(0,3)
                inicio = time.time()
            estado = com.rx.getIsEmpty()

        rxBuffer, rxTipo, rxErro, rxPacote, maxPacotes = com.rx.getNData()
        if rxTipo == 4:
            print("-------------------------")
            print("Chegou 4")
            bufferFinal = bytearray()
            for i in range(maxPacotes):
                if rxPacote == i:
                    if rxErro == 0:
                        acknack = 5
                        time.sleep(1)
                        com.sendData(0,acknack)
                        print("-------------------------")
                        print("Enviou 5")
                        bufferFinal.extend(rxBuffer)
                        pontos += 1
                        #flagPay = True
                    #ADICIONAR ELIFs PARA UM NOVO ERRO TIPO 8 A SER ENVIADO
                    else:
                        acknack = 6
                        time.sleep(1)
                        com.sendData(0,acknack,rxPacote)
                        print("-------------------------")
                        print("Enviou 6,pedindo {}".format(rxPacote))
                        #flagPay = False

                    com.rx.clearBuffer()

                    inicio = time.time()
                    timeout = 0
                    while com.rx.getIsEmpty():
                        timeout = time.time() - inicio
                        if timeout >= 5:
                            com.sendData(0,acknack)
                            inicio = time.time()
                        estado = com.rx.getIsEmpty()

                    rxBuffer, rxTipo, rxErro, rxPacote, maxPacotes = com.rx.getNData()
                
                else:
                    time.sleep(1)
                    com.sendData(0,8,i)
                    print("Envio 8, repedindo {}".format(i))

                    com.rx.clearBuffer()

                    inicio = time.time()
                    timeout = 0
                    while com.rx.getIsEmpty():
                        timeout = time.time() - inicio
                        if timeout >= 5:
                            com.sendData(0,8,i)
                            inicio = time.time()
                        estado = com.rx.getIsEmpty()

                    rxBuffer, rxTipo, rxErro, rxPacote, maxPacotes = com.rx.getNData()


            imgNova = open(imgEscrita,'wb')
            imgNova.write(bufferFinal)
            imgNova.close()
        if pontos == maxPacotes + 1:    
            flagPay = True

    if rxTipo == 7:
        print("-------------------------")
        print("Chegou 7")
        com.disable()

    # Encerra comunicação
    print("-------------------------")
    print("Comunicação encerrada")
    print("-------------------------")

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()