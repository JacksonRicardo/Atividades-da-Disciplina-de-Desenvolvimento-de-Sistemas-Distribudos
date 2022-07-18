############### Cliente TCP para mensagens. ###############
import socket
import sys

host = 'localhost'
port = 1234

# Cria um socket TCP.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 6666))
print('Conectado!!\n')

print('Para sair use CTRL+X e pressione enter')
msg = input()

try:
    while msg != '\x18':
        #Envia os dados
        s.sendall(msg.encode())

        #Recebe a resposta do servidor 
        data = s.recv(1024)
        print (data.decode())
        msg = input()
finally:
    print('Encerrando conexão... Tchau, Tchau!')
    s.close()

# print('Escreva uma mensagem de agradecimento pelo arquivo: \n')

############### Cliente UDP para mensagens de texto. ###############

 # host = gethostname()
 # port = 55555

 # print(f'HOST: {host}, PORT {port}')

# cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# cli.connect(('localhost', 7777))
# print('Conectado UDP!!\n')

# destino = ('localhost', 7777)
# while 1:
#     msg = input("Digite: ")
#     cli.send(msg.encode())

# print("Digite sua mensagem: \n")
# msg = input()

# cli.sendto(bytes(msg,"utf8"), destino)

# cli.close