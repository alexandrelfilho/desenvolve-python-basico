
# Solicita as idades de Juliana e Cris
idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))

# Verifica se pelo menos uma das duas pode entrar no bar
pode_entrar_no_bar = idade_juliana > 17 or idade_cris > 17
print(pode_entrar_no_bar)
