import random

def carregar_palavras(arquivo):
    """Carrega uma lista de palavras a partir de um arquivo, separadas por quebras de linha."""
    with open(arquivo, 'r') as f:
        palavras = [linha.strip() for linha in f if linha.strip()]
    return palavras

def carregar_estagios(arquivo):
    """Carrega os estágios do enforcado a partir de um arquivo."""
    with open(arquivo, 'r') as f:
        estagios = f.read().strip().split('\n\n')
    return estagios

def imprime_enforcado(estagios, erros):
    """Imprime o estágio do enforcado baseado no número de erros."""
    if 0 <= erros < len(estagios):
        print(estagios[erros])
    else:
        print("Número de erros inválido!")

def mostrar_progresso(palavra, letras_adivinhadas):
    """Mostra o progresso atual da palavra com base nas letras adivinhadas."""
    return ' '.join([letra if letra in letras_adivinhadas else '_' for letra in palavra])

def jogo_da_forca():
    palavras = carregar_palavras('gabarito_forca.txt')
    estagios = carregar_estagios('gabarito_enforcado.txt')

    palavra = random.choice(palavras)  # Escolhe uma única palavra aleatória
    letras_adivinhadas = set()
    erros = 0
    tentativas_maximas = 6  # Número máximo de tentativas

    print("Bem-vindo ao jogo da forca!")
    print(mostrar_progresso(palavra, letras_adivinhadas))
    
    while erros < tentativas_maximas:
        tentativa = input("Digite uma letra: ").lower()

        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue

        if tentativa in letras_adivinhadas:
            print("Você já tentou essa letra.")
            continue

        if tentativa in palavra:
            letras_adivinhadas.add(tentativa)
            print("Acertou!")
        else:
            erros += 1
            print("Errou!")
        
        progresso = mostrar_progresso(palavra, letras_adivinhadas)
        print(progresso)
        imprime_enforcado(estagios, erros)
        
        if '_' not in progresso:
            print("Parabéns! Você ganhou!")
            break
    else:
        print(f"Você perdeu! A palavra era '{palavra}'.")

if __name__ == "__main__":
    jogo_da_forca()
