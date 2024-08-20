import re

def eh_palindromo(frase):
    # Remove espaços, sinais de pontuação e converte para minúsculas
    frase_limpa = re.sub(r'[^a-zA-Z0-9]', '', frase).lower()
    return frase_limpa == frase_limpa[::-1]

while True:
    entrada = input('Digite uma frase (digite "fim" para encerrar): ')
    if entrada.lower() == 'fim':
        break
    if eh_palindromo(entrada):
        print(f'"{entrada}" é palíndromo')
    else:
        print(f'"{entrada}" não é palíndromo')
