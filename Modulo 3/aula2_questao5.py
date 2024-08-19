
# Solicita o gênero, idade e tempo de serviço
genero = input("Digite seu gênero (M ou F): ").strip().upper()
idade = int(input("Digite sua idade: "))
tempo_servico = int(input("Digite seu tempo de serviço (em anos): "))

# Verifica se a pessoa pode se aposentar
pode_aposentar = (
    (genero == "F" and idade > 60) or
    (genero == "M" and idade >= 65) or
    (tempo_servico >= 30) or
    (idade >= 60 and tempo_servico >= 25)
)

print(pode_aposentar)
