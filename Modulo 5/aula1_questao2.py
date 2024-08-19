import random
import math

# Solicita ao usuário o valor de n
n = int(input("Digite o valor de n: "))

# Gera n valores inteiros aleatórios entre 0 e 100
valores = [random.randint(0, 100) for _ in range(n)]

# Calcula a raiz quadrada da soma dos valores
soma = sum(valores)
raiz_quadrada = math.sqrt(soma)

# Exibe o resultado
print(f"A raiz quadrada da soma dos valores é: {raiz_quadrada:.2f}")
