import emoji

# Lista de emojis disponíveis
emojis_disponiveis = {
    "❤️": ":red_heart:",
    "👍": ":thumbs_up:",
    "🤔": ":thinking_face:",
    "🥳": ":partying_face:"
}

# Exibe a lista de emojis disponíveis
print("Emojis disponíveis:")
for emoji_char, emoji_code in emojis_disponiveis.items():
    print(f"{emoji_char} - {emoji_code}")

# Solicita uma frase codificada ao usuário
frase_codificada = input("Digite uma frase e ela será emojizada: ")

# Decodifica a frase usando a função emoji.emojize()
frase_emojizada = emoji.emojize(frase_codificada, use_aliases=True)

# Exibe a frase emojizada
print("Frase emojizada:")
print(frase_emojizada)
