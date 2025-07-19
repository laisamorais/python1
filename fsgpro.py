#Crie um programa que peça para o usuário digitar três notas individualmente
#  (uma por vez), faça a média e caso a média seja igual ou maior que 7,
#  mostre uma mensagem "Aprovado!" e a média. Caso seja menor que 7,
#  mostre uma mensagem "Reprovado!" e a média

valor1 = int(input("digite seu valor1: "))
valor2 = int(input("digite seu valor2: "))
valor3 = int(input("digite seu valor3: "))

media = (valor1 + valor2 + valor3)/3

if media < 7:
    print("reprovado!")

else :
    print("aprovado!")

print(f"sua media é igual: {media}")