#laborar um programa que alerte sobre os riscos de animais em extinção.
#  O usuário deve digitar o nome da espécie e a sua população (total de indivíduos).
#  Populações entre 0 e 500 indivíduos,
#  são classificadas como "Espécie criticamente em perigo", populações entre 501 e 1000
# indivíduos, são classificadas como "Espécie em perigo" e populações entre 1001 e 5000 
# indivíduos, são classificadas como "Espécie vulnerável!"


especie = input("digite sua especie: ")
populacao = int(input("digite seu populacao: "))

if populacao >1 and populacao < 500:
    print("Espécie criticamente em perigo!")

elif populacao >=501 and populacao <= 1000: 
    print("Espécie em perigo!")

elif populacao >= 1001 and populacao < 5000:
    print("Espécie vulnerável!")
else:
    print("especie segura!")
