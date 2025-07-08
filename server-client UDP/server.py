from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread

def handle_client(data, addr, socket_server):
    print(f"Recebi mensagem de {addr}: {data.decode()}")
    with open("log_servidor.txt", "a") as log:
        log.write(f"Cliente {addr} enviou: {data.decode()}\n")
    reply = data.decode()
    socket_server.sendto(reply.encode(), addr)

server_socket = socket(AF_INET, SOCK_DGRAM)

server_socket.bind(('127.0.0.1', 11708)) 

print('Sever online esperando cliente')

while True:
    socket_client, addr_client = server_socket.recvfrom(1024)
    Thread(target=handle_client, args=(socket_client, addr_client, server_socket)).start()
    

