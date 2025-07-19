# Crie uma função que receba um número inteiro e retorne o fatorial desse
#  número.
def calcularFatorial(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

# Entrada do usuário
fatorial = int(input("Qual número você deseja: "))

# Calcula e mostra o resultado
resultado = calcularFatorial(fatorial)
print(f"O fatorial de {fatorial} é: {resultado}")
