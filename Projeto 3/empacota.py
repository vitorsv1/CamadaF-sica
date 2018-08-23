import math

def main(dado):
    tipoEncode = "utf-8"
    sizeInteiro = len(dado)
    maxSize = 255 # 8 bits pra representar o tamanho do payload

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
        if atual != number:
            if atual == 0:
                adendo = 0
            else:
                adendo = 1
            carga = dado[(maxSize*atual+adendo):(maxSize*(atual+1))]
            size = maxSize
        else:
            carga = dado[(maxSize*atual+adendo):]
            size = sizeInteiro - (number - 1)*maxSize

        # HEAD
        tamanho = size

        # EOP
        info = 'final'

        # MONTANDO #
        head.extend(tamanho.to_bytes(1,'big')) 
        head.extend(atual.to_bytes(1,'big'))
        head.extend(number.to_bytes(1,'big'))

        pay.extend(bytes(carga))

        eop.extend(bytes(info,tipoEncode))

        msg.extend(head)
        msg.extend(pay)
        msg.extend(eop)
        # ADICIONA A VARIAVEL PARA O BUFFER
        envio.extend(msg)

        count = count - 1
    
    return(envio)

if __name__ == "__main__":
    main()