# Crie um programa com função que peça um número ao usuário até que
#  ele acerte um número secreto (ex: 42).
# A função deve dizer se o palpite está certo ou não e contar quantas
#  tentativas foram feitas.

numero = 0
correto = 45

while numero != correto:
    numero = int (input('Palpite: '))
    print(f"Você digitou: {numero}, está errado")

print(f'PARABÉNSSSS! Você acertou, é 45')