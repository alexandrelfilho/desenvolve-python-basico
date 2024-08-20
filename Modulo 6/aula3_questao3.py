import random

# Gera uma lista com 20 elementos entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

# Encontra o intervalo com maior quantidade de números negativos
max_negativos = 0
inicio_intervalo = 0
fim_intervalo = 0

for i in range(len(lista)):
    for j in range(i + 1, len(lista) + 1):
        intervalo = lista[i:j]
        negativos = sum(1 for x in intervalo if x < 0)
        if negativos > max_negativos:
            max_negativos = negativos
            inicio_intervalo = i
            fim_intervalo = j

# Remove o intervalo com maior quantidade de números negativos
del lista[inicio_intervalo:fim_intervalo]
print("Editada:", lista)