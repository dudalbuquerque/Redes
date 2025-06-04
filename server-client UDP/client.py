from socket import socket, AF_INET, SOCK_DGRAM

client_socket = socket(AF_INET, SOCK_DGRAM)
server_addr = ('127.0.0.1', 11708)

messages = ["Oi, server!", "Hello, server!", "Hi, server!"]

for msg in messages:
    client_socket.sendto(msg.encode(), server_addr)
    reply, _ = client_socket.recvfrom(1024)
    print(f"Resposta recebida do servidor: {reply.decode()}")