import re

# Define o nome do arquivo
arquivo = 'estomago.txt'

# Inicializa variáveis
total_linhas = 0
linha_max_caracteres = ''
mencoes_nonato = 0
mencoes_iria = 0

# Abre e processa o arquivo
with open(arquivo, 'r', encoding='utf-8') as file:
    linhas = file.readlines()
    
    # Imprime as primeiras 25 linhas
    print("Primeiras 25 linhas:")
    for i, linha in enumerate(linhas[:25]):
        print(linha.strip())
    print()  # Linha em branco para separar os resultados
    
    # Conta o número de linhas
    total_linhas = len(linhas)
    
    # Encontra a linha com maior número de caracteres
    linha_max_caracteres = max(linhas, key=len).strip()
    
    # Conta o número de menções aos nomes dos personagens
    for linha in linhas:
        mencoes_nonato += len(re.findall(r'\bNonato\b', linha, re.IGNORECASE))
        mencoes_iria += len(re.findall(r'\bÍria\b', linha, re.IGNORECASE))

# Imprime os resultados
print(f"Número total de linhas: {total_linhas}")
print(f"Linha com maior número de caracteres: {linha_max_caracteres}")
print(f"Número de menções ao nome 'Nonato': {mencoes_nonato}")
print(f"Número de menções ao nome 'Íria': {mencoes_iria}")