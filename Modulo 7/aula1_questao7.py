import random

def encrypt(lista_nomes):
    chave = random.randint(1, 10)
    nomes_criptografados = []
    for nome in lista_nomes:
        nome_criptografado = ''.join(
            chr(((ord(c) - 33 + chave) % 94) + 33) for c in nome
        )
        nomes_criptografados.append(nome_criptografado)
    return nomes_criptografados, chave

def main():
    nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
    nomes_criptografados, chave = encrypt(nomes)
    print(f"Chave aleatória: {chave}")
    print(f"Nomes criptografados: {nomes_criptografados}")

if __name__ == "__main__":
    main()