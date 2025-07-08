from socket import socket, AF_INET, SOCK_DGRAM
import random

# Configuração do servidor
HOST = 'localhost'
PORT = 12345

# Criação do socket UDP
cliente = socket(AF_INET, SOCK_DGRAM)

print("Cliente UDP iniciado. Respondendo automaticamente...\n")

# Envia mensagem inicial para o servidor
cliente.sendto("iniciar".encode(), (HOST, PORT))

for i in range(5): 
    pergunta, addr = cliente.recvfrom(1024)
    pergunta = pergunta.decode()
    print(pergunta)

    # Escolhe resposta aleatória
    resposta = random.choice(['A', 'B', 'C', 'D'])
    print(f"Resposta: {resposta}")

    # Envia resposta ao servidor
    cliente.sendto(resposta.encode(), (HOST, PORT))

# Fecha o socket
cliente.close()
print("Conexão encerrada.")
