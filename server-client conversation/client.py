import socket

# Cria o socket do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 12345))

print("Conectado ao servidor!")

# Envia e recebe mensagens
while True:
    msg = input("Cliente: ")
    cliente.send(msg.encode())
    if msg.lower() == "sair":
        break
    resposta = cliente.recv(1024).decode()
    print(f"Servidor: {resposta}")

cliente.close()
