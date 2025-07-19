#Faça um programa para ler o salário anual de um funcionário e o piso salarial mensal 
#da sua categoria. Mostrar o salário mensal do funcionário e dizer 
# se ele recebe de acordo com o piso (salário mensal igual ou maior que o piso da
#  categoria) ou se recebe abaixo do piso.

salario = int(input("digite seu salario anual: "))

piso = 4000

if salario < piso :
    print("recebe abaixo do piso salarial mensal")

else :
    print("recebe de acordo com o piso")

