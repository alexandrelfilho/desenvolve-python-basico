def obter_nome_mes(mes_numero):
    meses = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ]
    return meses[mes_numero - 1]

data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")
dia, mes, ano = map(int, data_nascimento.split('/'))

nome_mes = obter_nome_mes(mes)

print(f"Você nasceu em {dia} de {nome_mes} de {ano}.")
