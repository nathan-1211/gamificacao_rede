import socket
from crypto_utils import diffie_hellman, generate_shared_secret, caesar_cipher

# Configuração do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 5555))  # Escutando na porta 5555
server_socket.listen(1)

print("Servidor aguardando conexões...")
conn, addr = server_socket.accept()
print(f"Conexão estabelecida com {addr}")

# Troca de chaves Diffie-Hellman
private_key, public_key, prime, base = diffie_hellman()
conn.send(f"{public_key},{prime},{base}".encode())  # Envia a chave pública, primo e base
received_public_key = int(conn.recv(1024).decode())  # Recebe a chave pública do cliente

# Calcula o segredo compartilhado
shared_secret = generate_shared_secret(private_key, received_public_key, prime)
print(f"Segredo compartilhado estabelecido: {shared_secret}")

# Loop de comunicação
while True:
    encrypted_message = conn.recv(1024).decode()
    if not encrypted_message:
        break

    decrypted_message = caesar_cipher(encrypted_message, shared_secret, encrypt=False)
    print(f" Cliente: {decrypted_message}")

    reply = input("Servidor: ")
    encrypted_reply = caesar_cipher(reply, shared_secret, encrypt=True)
    print(f" Mensagem criptografada enviada: {encrypted_reply}")
    conn.send(encrypted_reply.encode())

conn.close()
server_socket.close()
 
