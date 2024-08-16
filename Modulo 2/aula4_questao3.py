
nome_produto1 = input("Digite o nome do produto 1: ")
preco_unitario1 = float(input("Digite o preço unitário do produto 1: "))
quantidade1 = int(input("Digite a quantidade do produto 1: "))

nome_produto2 = input("Digite o nome do produto 2: ")
preco_unitario2 = float(input("Digite o preço unitário do produto 2: "))
quantidade2 = int(input("Digite a quantidade do produto 2: "))

nome_produto3 = input("Digite o nome do produto 3: ")
preco_unitario3 = float(input("Digite o preço unitário do produto 3: "))
quantidade3 = int(input("Digite a quantidade do produto 3: "))

# Calcula o preço total
total = (preco_unitario1 * quantidade1) + (preco_unitario2 * quantidade2) + (preco_unitario3 * quantidade3)

# Formata o preço total com separador de milhar e duas casas decimais
total_formatado = f"R${total:,.2f}"

# Imprime o resultado
print(f"Total: {total_formatado}")
