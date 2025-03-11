import random

def diffie_hellman():
    """Realiza a troca de chaves Diffie-Hellman"""
    prime = 23  # Número primo público
    base = 5    # Base pública

    private_key = random.randint(1, prime - 1)  # Chave privada
    public_key = (base ** private_key) % prime  # Chave pública

    return private_key, public_key, prime, base

def generate_shared_secret(private_key, received_public_key, prime):
    """Gera o segredo compartilhado"""
    return (received_public_key ** private_key) % prime

def caesar_cipher(text, key, encrypt=True):
    """Aplica a Cifra de César"""
    shift = key % 26  # Garante que a chave está dentro do intervalo do alfabeto
    if not encrypt:
        shift = -shift  # Para decriptografar, deslocamos para trás

    result = ""
    for char in text:
        if char.isalpha():  # Apenas letras são alteradas
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Mantém caracteres não alfabéticos inalterados
    return result
 
