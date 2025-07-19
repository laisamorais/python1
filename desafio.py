# Solicitar uma quantidade de notas ao usuário e
# repetir um loop com for baseado na quantidade
# informada.
# Dentro do for, perguntar a nota e adicionar
# numa soma de notas.
# Ao final da repetição informar a media das notas



SomaDasNotas = 0
quantidade = int(input("quantas notas o usuario pretende somar:  "))

for contador in range (1, quantidade +1):
    notas = int(input("digite uma nota: "))
    SomaDasNotas = SomaDasNotas + notas 

media = SomaDasNotas / contador
print(f"a sua media é:  {media}")
