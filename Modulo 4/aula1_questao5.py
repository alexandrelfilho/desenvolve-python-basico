
N = int(input("Digite a quantidade de respondentes: "))
soma_idades = 0
cont = 0

while cont < N:
    idade = int(input("Digite a idade: "))
    soma_idades += idade
    cont += 1

media_idades = soma_idades / N
print(f"Média das idades: {media_idades:.2f}")
