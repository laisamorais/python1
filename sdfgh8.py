#|Pedir 2 números para o usuário e mostrar qual é o maior e qual é o menor
#  ou se são iguais.

valor1 = float(input("digite seu valor1: "))
valor2 = float(input("digite seu valor2: "))

if valor1 > valor2:
    print("valor1 é maior!")

elif valor2 == valor1:
    print("são iguais!")

else:
    print("valor2 é maior!")
