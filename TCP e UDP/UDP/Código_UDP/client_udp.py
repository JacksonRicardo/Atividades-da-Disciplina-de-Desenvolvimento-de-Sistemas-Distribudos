############### Cliente UDP para mensagens. ###############
import socket
import sys

host = 'localhost'
port = 6666

# Cria um socket UDP/IP.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Conectado!!\n')

print('Para sair use CTRL+X e pressione enter')

print('Digite sua mensagem: ')
msg = input()


while msg != '\x18':
    s.sendto(msg.encode(), (host, port)) 
    msg = input()

print('Encerrando conexão... Tchau, Tchau!')
s.close()