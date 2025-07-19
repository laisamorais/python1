#Numa competição de arremesso de peteca, o competidor tem direito a 3 arremessos
#  para que a peteca caia em um alvo com áreas e pontuações de 0 a 5, 
# sendo 5 no centro e 0 fora do alvo. 
# 
# Faça um programa que pergunte
#  a pontuação de cada arremesso e ao final mostre o resultado (soma dos pontos) e a 
# classifição: 15 pontos (deus da peteca), de 14 a 10 (petequeiro profissa), de 9 a 5
#  (petequeiro de final de semana), de 4 a 1 (pseudo-petequeiro) e 0 pontos
#  (nunca petequeiro).


ponto1= float(input("digite a pontuação: "))
ponto2= float(input("digite a pontuação: "))
ponto3= float(input("digite a pontuação: "))

SomaDosPontos = ponto1 + ponto2 + ponto3
if SomaDosPontos >= 15:
    print("Deus da peteca!")

elif SomaDosPontos >=10 and SomaDosPontos <15:
    print("petequeiro profissa!")
elif SomaDosPontos <10 and SomaDosPontos <6:
    print("petequeiro de final de semana!")
elif SomaDosPontos <5 and SomaDosPontos >0:
    print("pseudo-petequeiro!")

else:
    print("nunca petequeiro!")

print(f"a soma é:  {SomaDosPontos}")

