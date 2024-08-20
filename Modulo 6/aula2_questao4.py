# Recebe a quantidade de elementos e os elementos da lista 1
n1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = [int(input(f"Digite o elemento {i + 1} da lista 1: ")) for i in range(n1)]

# Recebe a quantidade de elementos e os elementos da lista 2
n2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = [int(input(f"Digite o elemento {i + 1} da lista 2: ")) for i in range(n2)]

# Intercala os elementos das duas listas
lista_intercalada = []
for i in range(max(n1, n2)):
    if i < n1:
        lista_intercalada.append(lista1[i])
    if i < n2:
        lista_intercalada.append(lista2[i])

# Imprime a lista intercalada
print("Lista intercalada:", lista_intercalada)
