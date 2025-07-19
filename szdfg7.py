# Criar um programa para calcular a densidade demográfica (habitantes por quilômetro quadrado) de uma região. 
# Sendo, densidade igual a população (total de habitantes) dividida pela área 
# (metros quadrados). Mostrar mensagens para densidade alta (maior que 100), 
# média (entre 25 e 100),
#  baixa (menor que 25).

densidade= float(input("digite a densidade da sua região: "))
populacao = int(input("digite a população da sua região: "))
area = float(input("digite a área da sua região: "))
DensidadeDemografica = populacao/area

if DensidadeDemografica> 100:
    print("densidade alta")

elif DensidadeDemografica > 25 and DensidadeDemografica < 100:
    print(" densidade média")
else:
    print("densidade baixa")
