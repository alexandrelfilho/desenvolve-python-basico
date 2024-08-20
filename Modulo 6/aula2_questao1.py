import random

# Gera 20 valores aleatórios entre -100 e 100
valores = [random.randint(-100, 100) for _ in range(20)]

# Imprime a lista ordenada sem modificar a lista original
print("Lista ordenada:", sorted(valores))

# Imprime a lista original
print("Lista original:", valores)

# Encontra e imprime o índice do maior valor da lista
maior_valor = max(valores)
indice_maior = valores.index(maior_valor)
print("Índice do maior valor:", indice_maior)

# Encontra e imprime o índice do menor valor da lista
menor_valor = min(valores)
indice_menor = valores.index(menor_valor)
print("Índice do menor valor:", indice_menor)
