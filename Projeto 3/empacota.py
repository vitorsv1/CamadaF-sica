import math

def geral(dado):
    tipoEncode = "utf-8"
    sizeInteiro = len(dado)
    maxSize = 65535 # 16 bits pra representar o tamanho do payload

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


        # HEAD
        #So foi dado extend

        # EOP
        primeiro = 255
        segundo = 254
        terceiro = 253
        quarto = 252

        # MONTANDO #
        head.extend(size.to_bytes(2,'big')) 
        head.extend(atual.to_bytes(1,'big'))
        head.extend((number-1).to_bytes(1,'big'))

        pay.extend(bytes(carga))

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
    print(envio)
    return(envio)

if __name__ == "__main__":
    imgLida = "C:/Users/Mateus Enrico/Documents/Insper/CamadaFisica/Projeto 3/img/x.png"
    img = open(imgLida,'rb')
    geral(img.read())