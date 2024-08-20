def substituir_vogais(frase):
    vogais = 'aeiouAEIOU'
    return ''.join('*' if char in vogais else char for char in frase)

frase = input("Digite uma frase: ")
frase_modificada = substituir_vogais(frase)

print(f"Frase modificada: {frase_modificada}")
