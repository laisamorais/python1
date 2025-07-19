# uma feira de livros está fazendo promoção onde na compra de 3 livros,
#  o(a) comprador(a) ganha 15% de desconto.
#  Criar um programa que receba os valores dos 3 livros e mostra na tela o total dos livros
#  sem desconto e com desconto.

livro1 = float(input("digite o valor do livro1: "))
livro2 = float(input("digite o valor do livro2: "))
livro3 = float(input("digite o valor do livro3: "))
ComDesconto = (livro1+livro2+livro3) * 15/100
SemDeconto = livro1+ livro2+livro3
print(f" o seu pagamento com o desconto é:   {ComDesconto}")
print(f" o seu pagamento sem o desconto é:   {SemDeconto}")
