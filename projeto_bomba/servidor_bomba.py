# servidor_bomba.py
import socket
import threading
from criptografia import cifra_cesar
import time

# Configurações do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432        # Porta do servidor

# Mensagem original e chave
mensagem_original = "DESATIVAR123"
chave = 9
mensagem_criptografada = cifra_cesar(mensagem_original, chave)

# Função para iniciar o temporizador da bomba
def temporizador_bomba():
    print("Bomba ativada! Você tem 5 minutos para desativá-la.")
    time.sleep(300)  # 5 minutos em segundos
    print("Boom! A bomba explodiu.")
    exit()

# Função para lidar com a conexão do cliente
def handle_cliente(conn, addr):
    print(f"Conexão estabelecida com {addr}")
    conn.sendall(mensagem_criptografada.encode())

    # Recebe a chave do cliente
    chave_usuario = conn.recv(1024).decode()
    if chave_usuario.isdigit() and int(chave_usuario) == chave:
        conn.sendall("Bomba desativada! Parabéns!".encode())
        print("Bomba desativada pelo cliente.")
        exit()
    else:
        conn.sendall("Boom! A bomba explodiu.".encode())
        print("Bomba explodiu.")
        exit()

# Inicia o servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor iniciado em {HOST}:{PORT}. Aguardando conexão...")

    # Inicia o temporizador da bomba em uma thread separada
    threading.Thread(target=temporizador_bomba).start()

    # Aceita conexões de clientes
    conn, addr = s.accept()
    handle_cliente(conn, addr) 
