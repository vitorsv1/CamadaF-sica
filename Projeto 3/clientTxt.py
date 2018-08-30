
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
    
    data = bytearray()
    c0 = 83
    c1 = 255
    c2 = 254
    c3 = 253
    c4 = 252
    c5 = 42

    data.extend(c0.to_bytes(1,'big'))
    data.extend(c1.to_bytes(1,'big'))
    data.extend(c2.to_bytes(1,'big'))
    data.extend(c3.to_bytes(1,'big'))
    data.extend(c4.to_bytes(1,'big'))
    data.extend(c5.to_bytes(1,'big'))

    txBuffer = data
    txLen    = len(txBuffer)
    print("Tempo esperado")
    print("{} s".format(txLen*10/com.baudrate))

    # Transmite dado
    print("tentado transmitir .... {} bytes".format(txLen))
    com.sendData(txBuffer)
    print(txBuffer)
    # Atualiza dados da transmissão
    txSize = com.tx.getStatus()

    # Encerra comunicação
    print("-------------------------")
    print("Comunicação encerrada")
    print("-------------------------")
    com.disable()

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
