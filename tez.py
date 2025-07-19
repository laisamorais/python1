def maior_numero():
    n = int(input("Quantos números você vai digitar? "))
    maior = ""  
    
    for i in range(n):
        num = float(input(f"Digite o número {i+1}: "))
        
        if (maior is "") or (num > maior):
            maior = num
    
    return maior

resultado = maior_numero()
print("O maior número digitado foi:", resultado)
