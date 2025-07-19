#Criar um programa que pergunte o nome e a idade da pessoa, 
# e se tem comorbidade (S ou N). Mostrar mensagem "Pode se vacinar!" 
# caso a idade seja maior ou igual a 60 ou tenha comorbidade. 
# Caso contrário, mostrar mensagem "Não pode se vacinar!".

nome = input("digite seu nome : ")
comorbidade = input("digite  se tem comorbidades S ou N: ")
idade = int(input("digite sua idade : "))


if comorbidade == "n" or idade <= 60: 
    print("nao pode se vacinar")

else:
    print(" pode se vacinar")

