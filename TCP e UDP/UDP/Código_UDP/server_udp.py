############### Servidor UDP para para mensagens ###############
import socket
import sys

# Deixar vazio para receber conexões fora da rede local
host = ''

# Porta onde o servidor irá escutar
port = 6666

# Cria um socket 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Garante que o socket será destruído (podendo ser reusado) após uma interrupção da execução 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Associa o socket a porta
s.bind((host, port))

while True:
    print("Esperando por conexões...")
    # Aceita conexões
    data, host = s.recvfrom(1024) 
    
    print('Recebido: ', data, '\nOuvindo na porta: ', host)