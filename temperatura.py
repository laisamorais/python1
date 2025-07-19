# Crie uma função que receba uma temperatura em Celsius 
# e retorne a conversão para Fahrenheit.
# Use a fórmula: F = C * 1.8 + 32.

temp = float(input("digite uma temperatura em celsius: "))
temp2 = (temp * 1.8) + 32

def conversãoParaFahrenheitFunction():
    
    print(f'sua temperatura é:  {temp2}')

conversãoParaFahrenheitFunction()