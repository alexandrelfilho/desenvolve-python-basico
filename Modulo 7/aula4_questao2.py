import re

# Define os nomes dos arquivos
arquivo_entrada = "frase.txt"
arquivo_saida = "palavras.txt"

# Lê o conteúdo do arquivo "frase.txt"
with open(arquivo_entrada, "r") as arquivo:
    conteudo = arquivo.read()

# Remove espaços em branco e caracteres não alfabéticos
palavras = re.findall(r'\b\w+\b', conteudo)

# Salva as palavras em "palavras.txt"
with open(arquivo_saida, "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")

# Lê e imprime o conteúdo do arquivo "palavras.txt"
with open(arquivo_saida, "r") as arquivo:
    print(arquivo.read())
