import socket
from crypto_utils import diffie_hellman, generate_shared_secret, caesar_cipher

# Configuração do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5556))  # Conecta ao servidor

# Recebe a chave pública do servidor
server_data = client_socket.recv(1024).decode()
server_public_key, prime, base = map(int, server_data.split(","))

# Troca de chaves Diffie-Hellman
private_key, public_key, _, _ = diffie_hellman()
client_socket.send(str(public_key).encode())  # Envia sua chave pública

# Calcula o segredo compartilhado
shared_secret = generate_shared_secret(private_key, server_public_key, prime)
print(f" Segredo compartilhado estabelecido: {shared_secret}")

# Loop de comunicação
while True:
    message = input("Cliente: ")
    encrypted_message = caesar_cipher(message, shared_secret, encrypt=True)
    print(f" Mensagem criptografada enviada: {encrypted_message}")
    client_socket.send(encrypted_message.encode())

    encrypted_reply = client_socket.recv(1024).decode()
    decrypted_reply = caesar_cipher(encrypted_reply, shared_secret, encrypt=False)
    print(f" Servidor: {decrypted_reply}")

client_socket.close()
 
