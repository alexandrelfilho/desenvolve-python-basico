import os

# Solicita uma frase ao usuário
frase = input("Digite uma frase: ")

# Define o nome do arquivo e salva a frase
nome_arquivo = "frase.txt"
with open(nome_arquivo, "w") as arquivo:
    arquivo.write(frase)

# Obtém o caminho completo do arquivo
caminho_completo = os.path.abspath(nome_arquivo)
print(f"Frase salva em {caminho_completo}")
