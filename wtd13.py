# Valor fixo do frete
frete = 12.50

# Solicita o valor da compra
valor_compra = float(input("Digite o valor da compra: R$ "))

# Exibe as categorias de assinante
print("\nSelecione a categoria de assinante:")
print("1) Assinante Premium (20% de desconto + frete grátis)")
print("2) Assinante Gold (20% de desconto + paga frete)")
print("3) Assinante Silver (10% de desconto + paga frete)")
print("4) Não assinante (sem benefícios)")

# Solicita a categoria
categoria = int(input("Digite o número da categoria (1 a 4): "))

# Aplica os descontos e o frete conforme a categoria
if categoria == 1:
    desconto = valor_compra * 0.20
    valor_final = valor_compra - desconto
    print(f"\nVocê é Assinante Premium. Desconto de R$ {desconto:.2f} e frete grátis.")
elif categoria == 2:
    desconto = valor_compra * 0.20
    valor_final = (valor_compra - desconto) + frete
    print(f"\nVocê é Assinante Gold. Desconto de R$ {desconto:.2f} + frete de R$ {frete:.2f}.")
elif categoria == 3:
    desconto = valor_compra * 0.10
    valor_final = (valor_compra - desconto) + frete
    print(f"\nVocê é Assinante Silver. Desconto de R$ {desconto:.2f} + frete de R$ {frete:.2f}.")
elif categoria == 4:
    desconto = 0
    valor_final = valor_compra + frete
    print(f"\nVocê não é assinante. Sem desconto. Frete de R$ {frete:.2f}.")
else:
    print("\nCategoria inválida. Tente novamente.")
    exit()

# Exibe o valor final da compra
print(f"Valor final da compra: R$ {valor_final:.2f}")