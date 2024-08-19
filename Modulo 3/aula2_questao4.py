
# Solicita a classe do personagem e os pontos de força e magia
classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ").strip().lower()
pontos_forca = int(input("Digite os pontos de força (de 1 a 20): "))
pontos_magia = int(input("Digite os pontos de magia (de 1 a 20): "))

# Verifica se os pontos de atributo são consistentes com a classe escolhida
if classe == "guerreiro":
    atributos_validos = (pontos_forca >= 15) and (pontos_magia <= 10)
elif classe == "mago":
    atributos_validos = (pontos_forca <= 10) and (pontos_magia >= 15)
elif classe == "arqueiro":
    atributos_validos = (pontos_forca > 5 and pontos_forca <= 15) and (pontos_magia > 5 and pontos_magia <= 15)
else:
    atributos_validos = False

print("Pontos de atributo consistentes com a classe escolhida:", atributos_validos)
