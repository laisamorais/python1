# Programar um pequeno sistema utilizando função. 
# O usuário deve digitar o número base e o seu expoente. 
# A função deve retornar o resultado da exponenciação.

def calcular_exponenciacao(base, expoente):
  """
  Calcula a exponenciação de um número base elevado a um expoente.

  Args:
    base: O número base.
    expoente: O expoente.

  Returns:
    O resultado da exponenciação.
  """
  return base ** expoente

# Solicita ao usuário para digitar o número base
while True:
    try:
        num_base = float(input("Digite o número base: "))
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para a base.")

# Solicita ao usuário para digitar o expoente
while True:
    try:
        num_expoente = float(input("Digite o expoente: "))
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para o expoente.")

# Chama a função para calcular o resultado
resultado = calcular_exponenciacao(num_base, num_expoente)

# Exibe o resultado
print(f"\nO resultado de {num_base} elevado a {num_expoente} é: {resultado}")