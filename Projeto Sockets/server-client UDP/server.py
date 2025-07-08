from socket import socket, AF_INET, SOCK_DGRAM
import time

# Dados do quiz
perguntas = {
    'Qual o nome do livro escrito por Barney?': ['The Rulebook', 'The Playbook', 'The Brobook', 'The Wait For It Book'],
    'Qual é o bordão mais famoso do Barney?': ['True story', 'Legend — wait for it — dary', 'Suit up', 'High five'],
    'Qual o nome da filha de Barney?': ['Ellie', 'Lily', 'Sarah', 'Tracy'],
    'O que geralmente motiva Barney a dizer “Challenge accepted”?': ['Uma aposta de dinheiro', 'Uma missão impossível ou absurda', 'Uma briga com o Ted', 'Um pedido da Robin'],
    'Onde Barney trabalha durante a maior parte da série?': ['National Savings Bank', 'Empire Bank', 'Goliath National Bank', 'Allied Trust']
}
Num_client = 2
respostas_corretas = ['B', 'B', 'A', 'B', 'C']
cliente_respostas = {i: [] for i in range(5)} 
clientes = [] 
placar = {}

# Inicia socket UDP
servidor = socket(AF_INET, SOCK_DGRAM)
servidor.bind(('localhost', 12345))

print("Servidor UDP online. Esperando clientes...")

while len(clientes) < Num_client:
    msg, addr = servidor.recvfrom(1024)
    if addr not in clientes:
        clientes.append(addr)
        placar[addr] = 0.0
        print(f"Cliente {len(clientes)} registrado: {addr}")

for i, (pergunta, opcoes) in enumerate(perguntas.items()):
    mensagem = f"\nPergunta {i+1}:\n{pergunta}\n"
    for idx, opcao in enumerate(opcoes):
        letra = chr(ord('A') + idx)
        mensagem += f"{letra}) {opcao}\n"

    # Envia pergunta para todos os clientes
    for addr in clientes:
        servidor.sendto(mensagem.encode(), addr)

    # Recebe respostas de todos os clientes
    recebidas = 0
    while recebidas < 5:
        resposta, addr = servidor.recvfrom(1024)
        resposta = resposta.decode().strip().upper()
        cliente_respostas[i].append((addr, resposta))
        print(f"[{addr}] Respondeu: {resposta}")
        recebidas += 1

# Corrige e pontua
for i in range(5):
    respostas = cliente_respostas[i]
    correta = respostas_corretas[i]
    pontos = 1.0
    for addr, resposta in respostas:
        if resposta == correta and pontos > 0:
            placar[addr] += pontos
            pontos -= 0.1
        else:
            placar[addr] += 0.0

# Mostra placar
print("\nResultado Final: ")
for addr, score in placar.items():
    print(f"{addr}: {score:.1f} pontos")
