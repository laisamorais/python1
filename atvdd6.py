# Faça uma função que receba uma senha digitada pelo usuário e continue pedindo até que ele digite 
# a senha correta (“Python123”). Quando acertar, deve exibir uma mensagem de sucesso

senha = "Python123"
tentativa=input("digite sua senha: ")

def SenhaSeguraFunction(senha):
    

   if tentativa == senha:
        print("bem vindo usuario!!")     
   else:
        print("senha invalida!tente novamente: ")
    
SenhaSeguraFunction(senha)

