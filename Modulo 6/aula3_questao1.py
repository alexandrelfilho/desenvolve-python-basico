numeros = []
print("Digite pelo menos 4 números inteiros (digite 'fim' para encerrar):")

while True:
    entrada = input()
    if entrada.lower() == 'fim':
        if len(numeros) >= 4:
            break
        else:
            print("Por favor, digite pelo menos 4 números.")
            continue
    
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# Imprime a lista original
print("A lista original:", numeros)

# Imprime os 3 primeiros elementos
print("Os 3 primeiros elementos:", numeros[:3])

# Imprime os 2 últimos elementos
print("Os 2 últimos elementos:", numeros[-2:])

# Imprime a lista invertida
print("A lista invertida:", numeros[::-1])

# Imprime os elementos de índice par
print("Os elementos de índice par:", numeros[::2])

# Imprime os elementos de índice ímpar
print("Os elementos de índice ímpar:", numeros[1::2])