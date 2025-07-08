from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

# Perguntas e alternativas
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

# Função que envia as perguntas e processa as respostas
def handle_http_client(conn, addr, cliente_id):
    print(f"{cliente_id} conectado: {addr}")
    placar[cliente_id] = 0

    perguntas_lista = list(perguntas.items())

    for i, (pergunta, opcoes) in enumerate(perguntas_lista):
        letras = ['A', 'B', 'C', 'D']
        corpo = f"<html><body><h2>Pergunta {i+1}:</h2><p>{pergunta}</p><form method='POST'>"
        for j, opcao in enumerate(opcoes):
            corpo += f"<input type='radio' name='resposta' value='{letras[j]}'>{letras[j]}) {opcao}<br>"
        corpo += "<input type='submit' value='Responder'></form></body></html>"

        header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: " + str(len(corpo)) + "\r\n\r\n"
        conn.send((header + corpo).encode())

        resposta_http = conn.recv(1024).decode()
        if "\r\n\r\n" in resposta_http:
            corpo_resposta = resposta_http.split("\r\n\r\n")[1]
            resposta_cliente = corpo_resposta.split('=')[-1].strip().upper()
            print(f"[{cliente_id}] Respondeu: {resposta_cliente}")
            if resposta_cliente == respostas_corretas[i]:
                placar[cliente_id] += 1

    # Resultado final
    resultado = "<html><body><h2>Resultado Final</h2><ul>"
    for cid, pontos in placar.items():
        resultado += f"<li>{cid}: {pontos} pontos</li>"
    resultado += "</ul></body></html>"
    header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: " + str(len(resultado)) + "\r\n\r\n"
    conn.send((header + resultado).encode())
    conn.close()
    print(f"{cliente_id} finalizou.")

# Inicia o servidor HTTP
ss = socket(AF_INET, SOCK_STREAM)
ss.bind(('localhost', 8080))
ss.listen()
print("Servidor HTTP rodando em http://localhost:8080")

for i in range(NUM_CLIENTES):
    conn, addr = ss.accept()
    cliente_id = f"cliente_{i+1}"
    clientes_conectados.append((conn, cliente_id))
    Thread(target=handle_http_client, args=(conn, addr, cliente_id)).start()
