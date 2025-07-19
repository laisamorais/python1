def soma(num1, num2):
  return num1 + num2

def subtracao(num1, num2):
  return num1 - num2

def multiplicacao(num1, num2):
  return num1 * num2

def divisao(num1, num2):
  if num2 == 0:
    return "Erro: Não é possível dividir por zero!"
  else:
    return num1 / num2

print("--- Calculadora Básica ---")

while True:
  try:
    primeiro_numero = float(input("Digite o primeiro número: "))
    segundo_numero = float(input("Digite o segundo número: "))
  except ValueError:
    print("Entrada inválida. Por favor, digite apenas números.")
    continue

  print("\nEscolha a operação:")
  print("1 - Soma")
  print("2 - Subtração")
  print("3 - Multiplicação")
  print("4 - Divisão")

  operacao = input("Digite o número da operação (1/2/3/4): ")

  resultado = None

  if operacao == '1':
    resultado = soma(primeiro_numero, segundo_numero)
  elif operacao == '2':
    resultado = subtracao(primeiro_numero, segundo_numero)
  elif operacao == '3':
    resultado = multiplicacao(primeiro_numero, segundo_numero)
  elif operacao == '4':
    resultado = divisao(primeiro_numero, segundo_numero)
  else:
    print("Opção inválida. Por favor, escolha entre 1, 2, 3 ou 4.")

  if resultado is not None:
    print(f"\nResultado: {resultado}")

  continuar = input("\nDeseja fazer outro cálculo? (s/n): ")
  if continuar.lower() != 's':
    break

print("Obrigado por usar a calculadora!")