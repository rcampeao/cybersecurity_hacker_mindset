from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Gerar uma chave secreta
chave_secreta = get_random_bytes(16) # AES-128 bits

# Criptografar uma mensagem
cifra_aes = AES.new(chave_secreta, AES.MODE_EAX)
mensagem = b"Mensagem secreta"
nonce = cifra_aes.nonce
texto_cifrado, tag = cifra_aes.encrypt_and_digest(mensagem)
print(f"Texto cifrado: {texto_cifrado}")

# Descriptografar a mensagem
cifra_aes = AES.new(chave_secreta, AES.MODE_EAX, nonce=nonce)
texto_decifrado = cifra_aes.decrypt(texto_cifrado)
print(f"Texto decifrado: {texto_decifrado}")
