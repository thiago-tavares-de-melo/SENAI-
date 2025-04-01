#-*- coding: UTF-8 -*-
cont = 1
print("Olá usuário, irei calcular a soma de zero até o número digitado")
def contador(valor):
    global cont

    for i in range(-1, valor + 1):
        cont = cont + i
        
valor = int(input("Digite o valor: "))
contador(valor)
print(f"O resultado é: {cont}")
    
