#Programa que calcula a area e o preço do terreno

#Define o valor em metros do comprimento do terreno, utilizado float pois estamos incluindo os centimetros
comp = float(input("Qual o comprimento do terreno? "))

#Define o valor em metros da largura do terreno.
larg = float(input("Qual a largura? "))

#Define o valor por m² da região do terreno
preco_m2 = float(input("Qual o preço por metro quadrado da região? ")) #podemos usar o preço baseado no exercício se necessário, preco_m2 = 512490.50/250

#Define qual a area do terreno
area_m2 = comp*larg

#Define o valor total do terreno baseado no m² da região e a area do terreno
preco_total = preco_m2*area_m2

#Mostra o resultado da area do terreno e seu preço total
print(f"O terreno possui {area_m2:.2f}m² e custa: R${preco_total:,.2f}")

