#criar um programa que simule o login de um roteador.
#  O username de usuário (username) é "admin" e a senha (password) "123". 
# Pedir ao usuário para digitar username e password.
#  Caso os dados estejam corretos, mostrar uma mensagem "Login efetuado!",
#  caso contrário "Login falhou!".
#  (DESAFIO: Mostrar mensagens específicas para erro de username,
#  de password ou de ambos).

username = input("digite seu username : ")
password = input("digite sua password: ")


if password == "123" and username=="admin":
    print("LOGIN EFETUADO!")

else:
    print("LOGIN FALHOU!")

