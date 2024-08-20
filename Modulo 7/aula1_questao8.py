def validar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"
    
    def calcular_digito(cpf, posicao):
        soma = 0
        multiplicador = posicao
        for i in range(posicao - 1):
            soma += int(cpf[i]) * multiplicador
            multiplicador -= 1
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    digito1 = calcular_digito(cpf, 10)
    digito2 = calcular_digito(cpf + str(digito1), 11)
    
    if cpf[-2:] == f"{digito1}{digito2}":
        return "Válido"
    else:
        return "Inválido"

def main():
    cpf = input("Digite o CPF na forma XXX.XXX.XXX-XX: ")
    print(validar_cpf(cpf))

if __name__ == "__main__":
    main()