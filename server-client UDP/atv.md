## Atividade de Introdução à programação com Sockets

Esta atividade tem como objetivo reforçar o que foi visto na aula de Introdução
à programação com Sockets. O objetivo é que vocês consigam criar uma aplicação do
tipo cliente-servidor utilizando sockets UDP.

### Instruções:
1. A aplicação desenvolvida neste exercício deve ser igual à desenvolvida
durante o laboratório TCP;
2. O servidor deve ser capaz de atender pelo menos dois clientes de
maneira simultânea;
3. A porta que deve ser utilizada será a combinação do número “1” + o dia
do seu aniversário + mês do seu aniversário:
    a. Dia do aniversário = 01, Mês do aniversário: 02:
    Porta = 10102

4. Cada cliente deverá enviar para o servidor, pelo menos 3 mensagens.
5. Todas às vezes que o cliente realizar uma solicitação o servidor deverá
enviar uma resposta, atendendo essa requisição;
6. A cada solicitação recebida o servidor deverá exibir no terminal qual o
cliente enviou a solicitação e qual a solicitação recebida, essas
informações deverão ser colocadas num arquivo para serem enviadas no
Classroom.

## Recomendações:
* Use a linguagem de programação que você já tem mais afinidade, caso
você não utilize nenhuma ainda, é recomendável que você utilize
Python.
* Utilize o wireshark para lhe ajudar no processo de verificação e
validação da sua aplicação.

O que deve ser anexado no classroom é um arquivo zipado contendo os
códigos do cliente e do servidor, um pdf contendo os prints de tela das solicitações do
cliente e dos logs impressos pelo servidor, e o arquivo pcap mostrando as trocas de
pacote entre os clientes e o servidor.