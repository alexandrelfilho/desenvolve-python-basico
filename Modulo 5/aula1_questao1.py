
# Solicita ao usuário para inserir dois números decimais
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Calcula a diferença absoluta entre os dois números e arredonda para duas casas decimais
diferenca_absoluta = abs(num1 - num2)
resultado = round(diferenca_absoluta, 2)

# Exibe o resultado
print(f"A diferença absoluta entre os números é: {resultado}")
