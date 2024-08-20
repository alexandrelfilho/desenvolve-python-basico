import random

# Gera um número aleatório entre 5 e 20
num_elementos = random.randint(5, 20)

# Gera valores aleatórios entre 1 e 10
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Imprime a lista elementos
print("Lista elementos:", elementos)

# Calcula e imprime a soma dos valores da lista
soma = sum(elementos)
print("Soma dos valores:", soma)

# Calcula e imprime a média dos valores da lista
media = soma / len(elementos)
print("Média dos valores:", media)
