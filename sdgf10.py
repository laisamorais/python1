#desenvolva um programa no qual o usuário deve digitar o nome e a idade de 3 pessoas.
#  Ao final mostrar a média de idade delas e a maior idade dentre essas pessoas.

idade1= int(input("digite a sua idade1: "))
nome1 =input("digite o seu nome: ")
idade2 = int(input("digite a sua idade2: "))
nome2 = input("digite o seu nome: ")
idade3 = int(input("digite a sua idade3: "))
nome3 = input("digite o seu nome: ")
media =( idade1 + idade2 + idade3)/3

if idade1 > idade2 and idade1 > idade3:
    print("idade1 é maior")

elif idade2 > idade1 and idade2 > idade3:
    print("idade2 é maior")

elif idade2 == idade1 and idade2 == idade3:
    print(" as idade são iguais")


else:
    print("idade3 é maior")

print(f"a média é:  {media}")
