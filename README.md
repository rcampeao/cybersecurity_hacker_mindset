# Exemplos Práticos para Curso de Cybersecurity

## Descrição
Este repositório contém exemplos práticos de códigos e recursos utilizados no curso de Cybersecurity. Cada diretório corresponde a uma aula ou tópico específico abordado no curso, fornecendo uma compreensão prática dos conceitos teóricos ensinados.

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
# instalar python3
sudo apt update
sudo apt upgrade
sudo apt install python3

# instalar o Poetry
curl -sSL https://install.python-poetry.org | python3 -

# criar um novo projeto com o Poetry
poetry new projeto_exemplo
cd projeto_exemplo

# instalar as dependências do projeto e criar o ambiente virtual
poetry install

# adicionar a biblioteca pycryptodome ao projeto
poetry add pycryptodome

# ativar o ambiente virtual do Poetry
poetry shell

# verificar se tudo funcionou:
# inicie o console interativo do Python e importe o módulo Crypto
# se não houver erro de importação, então funcionou
python
>>> from Crypto.Cipher import AES
>>> exit()
```

## Requisitos
+ Python 3.x
+ SO Linux
