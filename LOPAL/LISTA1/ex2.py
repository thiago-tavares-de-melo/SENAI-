#-*- coding: UTF-8 -*-
import math
print("""Olá usuário, irei ler um número e impirmir
a sua raiz caso ele for positivo, caso seja negativo irei
elevar ao quadrado""")
num = int(input("Digite o número: "))
r = math.sqrt(num) #raiz quadrada
p = num ** 2 #potência
if num >= 0:
    print("O resultado é:",r)
else:
    print("O resultado é:",p)
