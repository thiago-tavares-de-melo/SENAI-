#-*- coding: UTF-8 -*-
print("""Olá usuário, irei ler dois números e fazer a adição,
se a soma for maior que 20 irei adicionar 8, se for menor
ou igual a 20 irei subtrair 5.""")
num = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num + num2
menos = soma - 5
mais = soma + 8
if soma >= 21:
    print("O resultado é:",mais)
elif soma < 21:
    print("O resultado é:",menos)
else:
    print("Você digitou um número inválido")
    
