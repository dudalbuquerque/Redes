from socket import socket, AF_INET, SOCK_STREAM
import random
import time

# Configuração do servidor
HOST = 'localhost'
PORT = 12345

# Conecta ao servidor
cliente = socket(AF_INET, SOCK_STREAM)
cliente.connect((HOST, PORT))

print("Cliente conectado. Respondendo automaticamente...\n")

for i in range(5): 
    pergunta = cliente.recv(1024).decode()
    print(pergunta)

    resposta = random.choice(['A', 'B', 'C', 'D'])
    print(f"Resposta: {resposta}")
    ##time.sleep(random.uniform(1, 3))
    cliente.send(resposta.encode())

cliente.close()
print("Conexão encerrada.")
