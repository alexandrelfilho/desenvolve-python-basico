def main():
    numero = input("Digite o número: ")
    if len(numero) == 8:
        numero = '9' + numero
    if len(numero) == 9 and numero[0] != '9':
        print("Número inválido")
        return
    numero_formatado = f"{numero[:5]}-{numero[5:]}"
    print(f"Número completo: {numero_formatado}")

if __name__ == "__main__":
    main()