#Na sua lista de compras do mercado, constam apenas 3 itens: arroz,
#  batata palha e um suco de garrafa. Porém, você possui apenas uma nota de R$100 para pagar
# Faça um programa no qual# sejam digitados os valores dos itens e mostre na tela valor
#  que você deve receber (troco).

arroz =float(input("digite um valor para o arroz: "))
bat_palha =float(input("digite um valor para a batata palha: "))
suco =float(input("digite um valor para o suco: "))
valor_total = arroz+bat_palha+suco
troco =  100 - valor_total 
print(f"o troco vai ser:   {troco}  ")
print(f"o valor vai ser:  {valor_total}")