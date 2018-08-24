# LER 65536 BITS!!!!!!!!!!!!!!!!!!!! O tamanho reflete na representacao em hexa, mas nao na contagem necessaria

import math

def desempacota(dado):
    # Info
    headSize = 4
    eopSize = 4
  
    # Info de EOP
    confirmaEop = [255, 254, 253, 252]
  
    count = 0
    head = bytearray()
    pay = bytearray()
    eop = bytearray()
  
    for i in dado:
        while count < headSize:
            head.extend(bytes(i))
            print(i)
            print(head)
            count += 1
        tamanho = head[0] * 256 + head[1]
        pacote = head[2]
        maxPacotes = head[3]

    count = 0
    for i in dado:    
        if count >= headSize & count < (headSize + tamanho):
            pay.extend(bytes(i))
        elif count >= (headSize + tamanho) & count < (tamanho + headSize + eopSize):
            eop.extend(bytes(i))
        else:
            break
        count += 1
    
    pontos = 0
    correto = False
    corretoEop = False
    corretoPay = False

    for i in range(len(eop)):
        if eop[i] == confirmaEop[i]:
            pontos += 1 
    if pontos == 4:
        corretoEop = True

    if len(head) + len(pay) + len(eop) == tamanho + headSize + eopSize:
        corretoPay == True
    
    if corretoPay & corretoEop:
        correto = True

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

    return(envio)