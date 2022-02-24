import socket as sk
import threading as thr


porta = 8080
ip_servidor = "192.168.0.103"

servidor = sk.socket(sk.AF_INET, sk.SOCK_STREAM) #criando Socket TCP IPV4
servidor.bind((ip_servidor, porta))
servidor.listen()

mensagens = []
conexoes = []
clientes = []

def mensagem_todos(mensagem, conexao): #Enviar mensagens para todos os usuarios conectados
    global conexoes
    for conexao in conexoes:
        conexao.send(mensagem.encode('utf-8'))

def mensagem_client(conexao, endereco):
    print("O endereço", endereco,"acabou de se conectar")
    conexoes.append(conexao)
    global mensagens
    global clientes
    nickname = '?'
    while True:
        try:
            mensagem = conexao.recv(1024).decode('utf-8')
            if(mensagem):
                if(mensagem.startswith("nickname=")):
                    mensagem = mensagem.split("=")
                    nickname = mensagem[1]
                    clientes.append(nickname)
                    
                elif(mensagem.startswith("mensagem=")):
                    mensagem = mensagem.split("=")
                    texto = nickname + ':'+ mensagem[1]
                    print(nickname,"digitou", mensagem[1])
                    mensagens.append(texto)  
                    mensagem_todos(texto, conexao)

        except:
            print(nickname,"acabou de se desconectar do endereço:", endereco) # Encerra a trhead e remove a conexão do vetor de conexões
            conexoes.remove(conexao)
            break

def cria_thread():
    print("#Esperando conexões")
    while True:
        
        conexao , endereco = servidor.accept()
        thread = thr.Thread(target=mensagem_client, args=(conexao, endereco))
        thread.start()
           
cria_thread() #Inicia a Thread