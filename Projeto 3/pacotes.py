import math

tipoEncode = 'utf-8'
imgFile = "C:/Users/Mateus Enrico/Documents/Insper/CamadaFisica/Projeto 3/img/x.png"
img = open(imgFile,'rb')
dado = img.read()

def empacota(dado):
    sizeInteiro = len(dado)
    maxSize = 255 # 8 bits pra representar o tamanho do payload

    number = math.ceil(len(dado)/maxSize)
    count = number
    envio = bytearray()
    print('vai comecar')
    while count != 0:
        msg = bytearray()
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
            size = len(dado) - (number - 1)*maxSize

        # HEAD
        tamanho = size

        # EOP
        info = 'final'

        # MONTANDO #
        msg.extend(bytes(tamanho)) 
        msg.extend(bytes(atual))
        msg.extend(bytes(number))

        msg.extend(bytes(carga))

        msg.extend(bytes(info,encoding=tipoEncode))


        # ADICIONA A VARIAVEL PARA O BUFFER
        envio.extend(msg)
    
    print(envio)

empacota(dado)