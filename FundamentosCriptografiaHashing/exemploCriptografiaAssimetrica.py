from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Gerar um par de chaves (pública e privada)
chave = RSA.generate(2048)
chave_privada = chave.export_key()
chave_publica = chave.publickey().export_key()

# Criptografar uma mensagem com a chave pública
mensagem = b"Mensagem secreta"
cifra_rsa = PKCS1_OAEP.new(RSA.import_key(chave_publica))
texto_cifrado = cifra_rsa.encrypt(mensagem)
print(f"Texto cifrado: {texto_cifrado}")

# Descriptografar a mensagem com a chave privada
cifra_rsa = PKCS1_OAEP.new(RSA.import_key(chave_privada))
texto_decifrado = cifra_rsa.decrypt(texto_cifrado)
print(f"Texto decifrado: {texto_decifrado}")
