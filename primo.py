# Crie uma função que receba um número inteiro e verifique se ele é primo.
#  A função deve retornar True se for primo,
#  e False se não for.

num = int(input("digite o numero: "))

def NumeroPrimoFunction(num):
    if num  % 2 == 0 and num != 2:
        print("numero não é primo!")
    
    else:
        print("numero é primo!")


NumeroPrimoFunction(num)