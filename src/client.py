import socket as sk
import threading as thr

porta = 8080
ip_servidor = "192.168.0.103"


print("Digite o nome que deseja usar:")
nome = input()
nome = "nickname=" + nome              #Indicando que o primeiro input será para indicar nome de usuário
conexao = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
conexao.connect((ip_servidor, porta))
conexao.send(nome.encode('utf-8'))

def receber_mensagem():         #Função para ficar "ouvindo" o servidor
    while True:
        mensagem = conexao.recv(1024).decode()
        print(mensagem)

def enviar_mensagem():           #Função para ficar enviando mensagens para o servidor
    while True:
        mensagem = input()
        mensagem = "mensagem=" + mensagem        #Padronizando a mensagem quando não é para indicar o nome de usuário
        conexao.send(mensagem.encode('utf-8'))       

def cria_thread2():
        t1 = thr.Thread(target = receber_mensagem)
        t2 = thr.Thread(target = enviar_mensagem)
        t1.start()
        t2.start()

cria_thread2()