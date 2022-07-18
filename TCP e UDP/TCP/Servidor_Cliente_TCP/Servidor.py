############### Servidor TCP para para mensagens ###############
import socket
import sys

# Deixar vazio para receber conexões fora da rede local
host = ''

# Porta onde o servidor irá escutar
port = 6666

# Cria um socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# garante que o socket será destruído (pode ser reusado) após uma interrupção da execução 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Associa o socket a porta
s.bind((host, port))

print('Ouvindo servidor TCP %s na porta %s' % (socket.gethostname(), port))

# Socket colocado no modo Servidor e com limite de 1 conexão.
s.listen(1) 

while True:
    print("Esperando por conexões...")
    connection, adress = s.accept() # Aceita conexões

    try:
        print ('Conectado!')
        while True:            
            data = connection.recv(1024).decode()
            print('Mensagem recebida e retornada...')
            resposta = 'Mensagem recebida pelo servidor: '
            reply = resposta.encode() + data.encode()
            if not data:
                break
            connection.sendall(reply)
    finally:
        connection.close() #Limpar a conecção.





############### Servidor UDP para arquivos. ###############

# host = gethostname() 
# port = 55555

# print(f'HOST: {host}, PORT {port}')

#serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#serv.bind(('localhost', 7777))

#print('Conexão alterada para UDP!\n')

#serv.listen(1) #Limite de acesso

# while 1:
#     con, adr = serv.accept()
#     while 1:
#         msg = con.recv(1024) #Recebe mensagem em bytes.
#         print(msg.decode()) #Decodifica a msg acima.

#msg, end_cliente = serv.recvfrom(1024)
#print("Mensagem recebida: \n")
#print("Recebi = ", msg, ", do cliente", end_cliente)

#serv.close()