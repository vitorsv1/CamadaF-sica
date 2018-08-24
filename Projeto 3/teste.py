import pacote

path = "C:/Users/Mateus Enrico/Documents/Insper/CamadaFisica/Projeto 3/img/x.png"
img = open(path,'rb')
data = img.read()

empacotado = pacote.empacota(data)

imgNova = "C:/Users/Mateus Enrico/Documents/Insper/CamadaFisica/Projeto 3/img/teste.png"
print(type(empacotado))

saida = pacote.desempacota(empacotado)