 
# criptografia.py
def cifra_cesar(texto, deslocamento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            resultado += chr((ord(char) - shift + deslocamento) % 26 + shift)
        else:
            resultado += char
    return resultado

def decifrar_cesar(texto_criptografado, deslocamento):
    return cifra_cesar(texto_criptografado, -deslocamento)
