from socket import socket, AF_INET, SOCK_STREAM

socket_client = socket(AF_INET, SOCK_STREAM)

socket_client.connect(('172.20.4.75', 12345))

request = 'Hello server'

socket_client.send(request.encode())

reply = socket_client.recv(1024)

print(f'Resposta recabida do server: {reply.decode()}')
