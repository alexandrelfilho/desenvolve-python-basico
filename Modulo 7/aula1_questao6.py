def encontrar_anagramas(frase, palavra_objetivo):
    palavras = frase.split()
    anagramas = []
    palavra_objetivo_sorted = ''.join(sorted(palavra_objetivo))
    for palavra in palavras:
        if ''.join(sorted(palavra)) == palavra_objetivo_sorted:
            anagramas.append(palavra)
    return anagramas

def main():
    frase = input("Digite uma frase: ")
    palavra_objetivo = input("Digite a palavra objetivo: ")
    anagramas = encontrar_anagramas(frase, palavra_objetivo)
    print(f"Anagramas: {anagramas}")

if __name__ == "__main__":
    main()