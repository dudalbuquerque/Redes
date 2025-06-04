import socket

# Cria o socket do servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("localhost", 12345))  # IP e porta
servidor.listen()

print("Servidor esperando conexão...")

# Aceita conexão
cliente, endereco = servidor.accept()
print(f"Conectado a {endereco}")

# Recebe e responde mensagens
while True:
    dados = cliente.recv(1024).decode()
    if dados.lower() == "sair":
        print("Conexão encerrada.")
        break
    print(f"Cliente: {dados}")
    resposta = input("Servidor: ")
    cliente.send(resposta.encode())

cliente.close()
servidor.close()
