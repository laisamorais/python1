# Criar um programa que informa quantos dias tem determinado mês
#  (desconsiderando ano bissexto) do ano. Deve ser perguntado ao usuário
#  o mês e a resposta deve ser numérica. Exemplo: Usuário digitou 3,
#  que corresponde a março. 
# Mostrar na tela "O mês possui 31 dias".

mes = int(input("Digite o número do mês (1 a 12): "))

# Dicionário com os meses, seus nomes e respectivos dias (ano não bissexto)
meses = {
    1: ("janeiro", 31),
    2: ("fevereiro", 28),  # Ano não bissexto
    3: ("março", 31),
    4: ("abril", 30),
    5: ("maio", 31),
    6: ("junho", 30),
    7: ("julho", 31),
    8: ("agosto", 31),
    9: ("setembro", 30),
    10: ("outubro", 31),
    11: ("novembro", 30),
    12: ("dezembro", 31)
}

# Verifica se o mês está no intervalo válido
if 1 <= mes <= 12:
    nome_mes, dias = meses[mes]
    print(f"O mês de {nome_mes} possui {dias} dias.")
else:
    print("Mês inválido. Por favor, digite um número entre 1 e 12.")
