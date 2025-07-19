
# Variável com o saldo inicial
saldo = 1000.00

# Solicita o número da conta bancária
conta = input("Digite o número da sua conta bancária: ")

# Exibe o menu de operações
print("\nEscolha a operação a ser realizada:")
print("1) Saldo")
print("2) Depósito")
print("3) Saque")

# Solicita a operação
operacao = int(input("Digite o número da operação desejada (1, 2 ou 3): "))

# Processamento da operação
if operacao == 1:
    # Mostrar saldo
    print(f"\nConta {conta} - Saldo atual: R$ {saldo:.2f}")

elif operacao == 2:
    # Depósito
    valor = float(input("Digite o valor a ser depositado: R$ "))
    if valor > 0:
        saldo += valor
        print(f"\nDepósito realizado com sucesso.")
        print(f"Conta {conta} - Saldo atualizado: R$ {saldo:.2f}")
    else:
        print("Valor inválido para depósito.")

elif operacao == 3:
    # Saque
    valor = float(input("Digite o valor a ser sacado: R$ "))
    if valor <= saldo and valor > 0:
        saldo -= valor
        print(f"\nSaque realizado com sucesso.")
        print(f"Conta {conta} - Saldo atualizado: R$ {saldo:.2f}")
    elif valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
    else:
        print("Valor inválido para saque.")

else:
    print("Operação inválida. Por favor, selecione 1, 2 ou 3.")
