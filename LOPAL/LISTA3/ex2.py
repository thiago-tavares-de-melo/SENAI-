#-*- coding: UTF-8 -*-
print("""Olá usuário, irei calcular o produto de todos os dígitos de um
número inteiro""")
contador = 1

def multiplicar(valor):
    global contador

    for i in range(1, valor + 1):
        contador *= i
        
valor = int(input("Digite o valor: "))
multiplicar(valor)

print(f"O resultado é: {contador}")
