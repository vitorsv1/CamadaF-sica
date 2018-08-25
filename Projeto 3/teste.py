import pacote

#path = "C:/Users/Mateus Enrico/Documents/Insper/CamadaFisica/Projeto 3/img/vai.png"
#img = open(path,'rb')
#data = img.read()


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

empacotado = pacote.empacota(data)
print(empacotado)
imgNova = "C:/Users/Mateus Enrico/Documents/Insper/CamadaFisica/Projeto 3/img/teste.png"

saida = pacote.desempacota(empacotado)
#print(saida)