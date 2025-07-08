from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time
perguntas = {
    'Qual o nome do livro escrito por Barney?': ['The Rulebook', 'The Playbook', 'The Brobook', 'The Wait For It Book'],
    'Qual é o bordão mais famoso do Barney?': ['True story', 'Legend — wait for it — dary', 'Suit up', 'High five'],
    'Qual o nome da filha de Barney?': ['Ellie', 'Lily', 'Sarah', 'Tracy'],
    'O que geralmente motiva Barney a dizer “Challenge accepted”?': ['Uma aposta de dinheiro', 'Uma missão impossível ou absurda', 'Uma briga com o Ted', 'Um pedido da Robin'],
    'Onde Barney trabalha durante a maior parte da série?': ['National Savings Bank', 'Empire Bank', 'Goliath National Bank', 'Allied Trust']
}
NUM_CLIENTES = 2
respostas_corretas = ['B', 'B', 'A', 'B', 'C'] 
clientes_conectados = []
placar = {}

def handle_client(socket_client, addr_client, client_id):
    print(f"Cliente {client_id} conectado: {addr_client}")
    placar[client_id] = 0.0

    cliente_respostas = {i: [] for i in range(5)}
    for i, (pergunta, opcoes) in enumerate(perguntas.items()):
        mensagem = f"\nPergunta {i+1}:\n{pergunta}\n"
        for indice, opcao in enumerate(opcoes):
            lista = ['A', 'B', 'C', 'D']
            letra = lista[indice]
            mensagem += f"{letra}) {opcao}\n"
        socket_client.send(mensagem.encode())
        inicio = time.time()
        resposta = socket_client.recv(1024).decode().strip().upper()
        fim = time.time()
        tempo_resposta = fim - inicio
        print(f"[{client_id}] Respondeu: {resposta}, Tempo resposta: {tempo_resposta}")


        if resposta == respostas_corretas[i]:
            print ('X')
        cliente_respostas[i].append((client_id, resposta))

    socket_client.close()
    print(f"Cliente {client_id} finalizou.")


socket_server = socket(AF_INET, SOCK_STREAM)
socket_server.bind(('', 12345))
socket_server.listen()
print("Servidor online. Aguardando conexões...")

for i in range(NUM_CLIENTES):
    socket_client, addr_client = socket_server.accept()
    cliente_id = f"cliente_{i+1}"
    clientes_conectados.append((socket_client, cliente_id))
    placar[cliente_id] = 0.0
    print(f"Cliente {cliente_id} conectado.")


for i in range(2): ##depende da quantidade de clientes
    socket_client, addr_client = socket_server.accept()
    cliente_id = f"cliente_{i+1}"
    clientes_conectados.append((socket_client, cliente_id))
    Thread(target=handle_client, args=(socket_client, addr_client, cliente_id)).start()

import time
time.sleep(10)

# Mostra resultado final
print("\nResultado Final")
for cliente_id, pontuacao in placar.items():
    print(f"{cliente_id}: {pontuacao:.1f} pontos")