def main():
    frase = input("Digite uma frase: ")
    vogais = 'aeiou'
    indices = [i for i, c in enumerate(frase) if c in vogais]
    print(f"{len(indices)} vogais")
    print(f"Índices {indices}")

if __name__ == "__main__":
    main()