# Escreva uma função que receba um número n e solicite n notas ao usuário,
#  calcule a média e retorne o resultado.
funçãoFunction = 0
loops = int (input('E aí, quantas notas? '))
for contador in range(loops):
  nota = int(input("Digite uma nota: "))
funçãoFunction = funçãoFunction + nota
media = funçãoFunction / contador
print(f'Média: {media: .2f}')
