
# Solicita ao usuário a avaliação do filme
avaliacao = int(input("Digite a avaliação do filme (1 a 5): "))

# Imprime a mensagem correspondente à classificação
if avaliacao == 5:
    print("Excelente!")
elif avaliacao == 4:
    print("Muito Bom!")
elif avaliacao == 3:
    print("Bom!")
elif avaliacao == 2:
    print("Regular.")
elif avaliacao == 1:
    print("Ruim.")
else:
    print("Avaliação inválida.")
