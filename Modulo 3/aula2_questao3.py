
# Solicita a idade, se já jogou pelo menos 3 jogos e quantas vezes venceu
idade = int(input("Digite sua idade: "))
jogou_3_jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ").strip() == "True"
venceu_jogos = int(input("Quantos jogos já venceu? "))

# Verifica se o participante é apto para ingressar no clube
apto_para_ingressar = (16 <= idade <= 18) and jogou_3_jogos and (venceu_jogos >= 1)
print("Apto para ingressar no clube de jogos de tabuleiro:", apto_para_ingressar)
