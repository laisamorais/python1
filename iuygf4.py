#fazer um programa no qual o usuário digite a sua altura e o seu peso,
#  ao final mostre o IMC (índice de massa corporal)
#  e uma mensagem se está abaixo do peso (IMC menor que 18),
#  na faixa de peso ideal (IMC de 18 a 25) ou acima do peso (IMC maior 25).
#  IMC = peso / (altura * altura).

altura =float(input("digite sua altura atual "))
peso = float(input("digite seu peso atual"))
 
IMC = peso/(altura*altura)

if IMC <=18:
 print(f"abaixo do peso {IMC}")

elif IMC >18 and IMC < 25:
  print(f"está de acordo com o peso {IMC}")

else:
   print(f"está acima do peso {IMC}")
