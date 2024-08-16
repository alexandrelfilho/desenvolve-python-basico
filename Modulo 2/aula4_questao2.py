#   Define o valor da temperatura em fahrenheit
f = int(input("Digite a temperatura em fahrenheit: "))

#   Faz a conversão de fahrenheit pra celsius
c = (f - 32) * (5 / 9)

#   Converte a temperatura em celsius para inteiro
cint = int(c)

#   Mostra a temperatura convertida de Fahrenheit para Celsius
print(f"{f} graus Fahrenheit são {cint} graus Celsius.")