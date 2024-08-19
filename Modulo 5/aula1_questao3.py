import random

# Gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

while True:
    # Solicita ao usuário para adivinhar o número
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    
    # Fornece feedback sobre o palpite
    if palpite < numero_secreto:
        print("Muito baixo, tente novamente!")
    elif palpite > numero_secreto:
        print("Muito alto, tente novamente!")
    else:
        print(f"Correto! O número é {numero_secreto}.")
        break
