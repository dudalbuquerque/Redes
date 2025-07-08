from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time

# Perguntas e respostas corretas
perguntas = {
    'Qual o nome do livro escrito por Barney?': ['The Rulebook', 'The Playbook', 'The Brobook', 'The Wait For It Book'],
    'Qual é o bordão mais famoso do Barney?': ['True story', 'Legend — wait for it — dary', 'Suit up', 'High five'],
    'Qual o nome da filha de Barney?': ['Ellie', 'Lily', 'Sarah', 'Tracy'],
    'O que geralmente motiva Barney a dizer “Challenge accepted”?': ['Uma aposta de dinheiro', 'Uma missão impossível ou absurda', 'Uma briga com o Ted', 'Um pedido da Robin'],
    'Onde Barney trabalha durante a maior parte da série?': ['National Savings Bank', 'Empire Bank', 'Goliath National Bank', 'Allied Trust']
}
respostas_corretas = ['B', 'B', 'A', 'B', 'C']
NUM_CLIENTES = 2
clientes_conectados = []
placar = {}

# Função para receber resposta de um cliente
def receber_resposta(sock, cliente_id, respostas_coletadas, i):
    inicio = time.time()
    resposta = sock.recv(1024).decode().strip().upper()
    fim = time.time()
    tempo = fim - inicio
    print(f"{cliente_id} Respondeu: {resposta} em {tempo*1000:.1f}ms")
    respostas_coletadas.append((cliente_id, resposta, tempo))

# Configura servidor
socket_server = socket(AF_INET, SOCK_STREAM)
socket_server.bind(('', 12345))
socket_server.listen()
print("Servidor online. Aguardando conexões...")

# Aguarda conexões de clientes
for i in range(NUM_CLIENTES):
    socket_client, addr_client = socket_server.accept()
    cliente_id = f"cliente_{i+1}"
    clientes_conectados.append((socket_client, cliente_id))
    placar[cliente_id] = 0.0
    print(f"Cliente {cliente_id} conectado.")

# Início do questionário
print("\n>> Vai começar o questionário agora!\n")

# Para cada pergunta
for i, (pergunta, opcoes) in enumerate(perguntas.items()):
    # Monta mensagem da pergunta
    mensagem = f"\nPergunta {i+1}:\n{pergunta}\n"
    for indice, opcao in enumerate(opcoes):
        lista_letra = ['A', 'B', 'C', 'D']
        mensagem += f"{lista_letra[indice]}) {opcao}\n"

    # Envia para todos os clientes
    for sock, _ in clientes_conectados:
        sock.send(mensagem.encode())

    # Coleta respostas com threads
    respostas_coletadas = []
    threads = []
    for sock, cid in clientes_conectados:
        t = Thread(target=receber_resposta, args=(sock, cid, respostas_coletadas, i))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    # Avalia pontuação
    correta = respostas_corretas[i]
    corretas = [r for r in respostas_coletadas if r[1] == correta]
    corretas.sort(key=lambda x: x[2])  # ordena por tempo

    pontos = 1.0
    for cid, _, _ in corretas:
        placar[cid] += pontos
        pontos = max(0.0, pontos - 0.1)

    # Placar parcial
    print("\nPlacar parcial:")
    for cid, p in placar.items():
        print(f"{cid}: {p:.1f} pontos")

# Finaliza quiz
print("\nResultado Final:")
for cid, p in placar.items():
    print(f"{cid}: {p:.1f} pontos")

# Encerra conexões
for sock, _ in clientes_conectados:
    sock.close()
