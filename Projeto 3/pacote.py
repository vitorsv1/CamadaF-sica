import math

def desempacota(dado):
    # Info
    headSize = 5
    eopSize = 4
  
    # Info de EOP
    confirmaEop = [255, 254, 253, 252]
  
    count = 0
    head = bytearray()
    pay = bytearray()
    eop = bytearray()
  
    for i in dado:
        if count < headSize:
            #print(i)
            if count == 0:
                head.extend(i.to_bytes(1,'big'))
            else:
                head.extend(i.to_bytes(2,'big'))
            count += 1
    tamanho = head[0]
    pacote = head[1] * 256 + head[2]
    maxPacotes = head[3] * 256 + head[4]
    #print(head)
    
    count = 1
    point = 0
    flagEop = 0
    correto = False
    corretoEop = False
    corretoPay = False

    for i in range(len(dado)):
        if i + 3 < len(dado):
            if dado[i] == 255 and dado[i+1] == 254 and dado[i+2] == 253 and dado[i+3] == 252:
                corretoEop = True
                flagEop = i
                break

    if (flagEop - headSize) == tamanho:
        corretoPay = True
    
    if corretoPay & corretoEop:
        correto = True

    if corretoPay:
        pay = dado[headSize-1:flagEop]
    if correto:
        print("envio correto")
        return pay
    else:
        if not corretoPay:
            print("erro no tamanho do payload")
        else:
            print("erro no EOP")
        return -1
        
def empacota(dado):
    tipoEncode = "utf-8"
    sizeInteiro = len(dado)
    maxSize = 255 # 16 bits pra representar o tamanho do payload

    number = math.ceil(sizeInteiro/maxSize)
    count = number
    envio = bytearray()
    print(sizeInteiro)
    print(number)
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
        head.extend(size.to_bytes(1,'big')) 
        head.extend(atual.to_bytes(2,'big'))
        head.extend((number-1).to_bytes(2,'big'))
        
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

    overhead = maxSize / (5 + maxSize + 4)
    print("Overhead: {}%".format(overhead*100))

    return(envio)