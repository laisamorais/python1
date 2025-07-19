# Pedir para o usuário digitar 1 numero, mostrar se é par ou impar e
#  se é positivo ou negativo.


num = int(input("digite seu numero"))

if num % 2 == 0 and num < 0:
 print(f"valor {num} é par e negativo")

elif num % 2 == 0 and num > 0:
  print(f"valor {num} é par e positivo")

elif num % 2 == 1 and num < 0:
 print(f"valor {num} impar e negativo")

else:
   print(f"valor {num} é impar e postivo ")

