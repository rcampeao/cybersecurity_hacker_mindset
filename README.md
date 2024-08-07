# Exemplos Práticos para o Curso de Cybersecurity (Hacker Mindset)

## Descrição
Este repositório contém exemplos práticos de códigos e recursos utilizados no curso de Cybersecurity (Hacker Mindset). Cada diretório corresponde a uma aula ou tópico específico abordado no curso, fornecendo uma compreensão prática dos conceitos teóricos ensinados.

## Conteúdo
+ S2 Aula 1: Fundamentos de Criptografia e Hashing
  + Exemplos de funções hash (MD5, SHA-1, SHA-256, SHA-384, SHA-512)
  + Scripts práticos usando bibliotecas como hashlib e OpenSSL
  + Demonstrações de criptografia simétrica e assimétrica
  + Implementações de cifras de César e Vigenère

## Recomendação:

### Ambientes Virtuais
+ Ambientes virtuais são recomendados para evitar problemas com pacotes pip de diferentes versões ou pacotes que se instalam na mesma pasta (por exemplo, pycrypto e pycryptodome). Usar um ambiente virtual permite que cada projeto tenha seu próprio conjunto de pacotes gerenciados individualmente.

+ Para instalar um ambiente virtual e configurá-lo, use os comandos a seguir:

```
# instalar python3 e pip3
sudo apt update
sudo apt upgrade
sudo apt install python3
sudo apt install python3-pip

# instalar virtualenv
pip3 install virtualenv

# instalar e criar um ambiente virtual na sua pasta de destino
mkdir pasta_destino
cd pasta_destino
python3 -m virtualenv .

# agora ative seu ambiente virtual e instale pycryptodome
source bin/activate
pip3 install pycryptodome

# verifique se tudo funcionou:
# inicie o console interativo do Python e importe o módulo Crypto
# se não houver erro de importação, então funcionou
python
>>> from Crypto.Cipher import AES
>>> exit()

# não se esqueça de desativar seu ambiente virtual
deactivate
```

## Requisitos
+ Python 3.x
+ SO Linux
