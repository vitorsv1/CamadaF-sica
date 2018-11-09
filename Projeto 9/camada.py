import socket

########
#https://wiki.python.org.br/SocketBasico
# modificado os inputs
#######
HOST = '127.0.0.1'     
PORT = 6969            
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
inp = True
while inp:
    mensagem = input("Digite o seu MecTrabFon: ")
    mensagem = bytearray(mensagem,"utf-8")
    tcp.send(mensagem)
    if mensagem == 'exit':
        inp = False
tcp.close()