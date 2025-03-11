# cliente_aluno.py
import socket
from criptografia import decifrar_cesar

# Configurações do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432        # Porta do servidor

# Conecta ao servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Recebe a mensagem criptografada
    mensagem_criptografada = s.recv(1024).decode()
    print(f"Mensagem interceptada: {mensagem_criptografada}")

    # Realiza a criptoanálise (força bruta)
    print("Realizando criptoanálise...")
    for deslocamento in range(26):
        mensagem_decifrada = decifrar_cesar(mensagem_criptografada, deslocamento)
        print(f"Deslocamento {deslocamento}: {mensagem_decifrada}")

    # Solicita a chave ao usuário
    chave_usuario = input("Digite a chave correta para desativar a bomba: ")

    # Envia a chave para o servidor
    s.sendall(chave_usuario.encode())

    # Recebe a resposta do servidor
    resposta = s.recv(1024).decode()
    print(resposta) 
