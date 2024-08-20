import random
from collections import Counter

# Preenche duas listas com 20 valores aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Cria uma terceira lista contendo a interseção (sem duplicatas) e ordena
interseccao = sorted(set([x for x in lista1 if x in lista2]))

# Conta as ocorrências de cada elemento em lista1 e lista2
contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)

# Imprime as listas
print("lista1 -", lista1)
print("lista2 -", lista2)
print("Interseccao -", interseccao)

# Imprime a contagem de cada elemento nas duas listas
print("Contagem")
for valor in interseccao:
    print(f"{valor}: (lista1={contagem_lista1[valor]}, lista2={contagem_lista2[valor]})")
