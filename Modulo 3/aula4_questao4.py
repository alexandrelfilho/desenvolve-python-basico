
# Solicita a distância da entrega e o peso do pacote
distancia = float(input("Digite a distância da entrega (em km): "))
peso = float(input("Digite o peso do pacote (em kg): "))

# Calcula o valor do frete com base na distância
if distancia <= 100:
    valor_frete = 1 * peso
elif 101 <= distancia <= 300:
    valor_frete = 1.50 * peso
else:
    valor_frete = 2 * peso

# Adiciona a taxa adicional para pacotes com peso superior a 10 kg
if peso > 10:
    valor_frete += 10

print(f"O valor do frete é: R${valor_frete:.2f}")