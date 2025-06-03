from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


def handle_client(addr_client, socket_client):
    print(f'recebi mensagem do client {addr_client}')
    req = socket_client.recv(1024)
    print(f'mensagem recebida do cliente {req.decode()}')
    reply_client = "hello, Client"
    socket_client.send(reply_client.encode())



socket_server = socket(AF_INET, SOCK_STREAM)

socket_server.bind(('', 12345)) ##IP ESTÁVEL

socket_server.listen() #escuta requisições

print('sever online esperando cliente')

for i in range(3):
    socket_client, addr_client = socket_server.accept() #aceita a comunicação do cliente, linha bloqueante 
    Thread(target= handle_client, args=(addr_client, socket_client)).start()
