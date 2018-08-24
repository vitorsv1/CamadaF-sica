import pacote

path = "C:/Users/Mateus Enrico/Documents/Insper/CamadaFisica/Projeto 3/img/vai.png"
img = open(path,'rb')
data = img.read()

empacotado = pacote.empacota(data)

imgNova = "C:/Users/Mateus Enrico/Documents/Insper/CamadaFisica/Projeto 3/img/teste.png"

saida = pacote.desempacota(empacotado)
print(saida)