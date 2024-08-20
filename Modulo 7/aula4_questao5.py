import csv

# Dados dos livros
livros = [
    ["O Guia do Mochileiro das Galáxias", "Douglas Adams", 1979, 224],
    ["Neuromancer", "William Gibson", 1984, 271],
    ["Duna", "Frank Herbert", 1965, 412],
    ["Fundação", "Isaac Asimov", 1951, 255],
    ["O Hobbit", "J.R.R. Tolkien", 1937, 310],
    ["O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", 1954, 423],
    ["Ender's Game", "Orson Scott Card", 1985, 324],
    ["Ready Player One", "Ernest Cline", 2011, 374],
    ["O Nome do Vento", "Patrick Rothfuss", 2007, 662],
    ["Mistborn: Nascença de um Império", "Brandon Sanderson", 2006, 541]
]

# Nome do arquivo
nome_arquivo = 'meus_livros.csv'

# Criando e escrevendo no arquivo CSV
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    
    # Escreve o cabeçalho
    writer.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])
    
    # Escreve as linhas de dados
    writer.writerows(livros)

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
