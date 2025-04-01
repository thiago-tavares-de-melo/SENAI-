#-*- coding: UTF-8 -*-
print("""Olá usuário, digite dois números inteiros e eu o informarei
se o primeiro é divisível pelo segundo""")
a = int(input("Digite o primeiro número:"))
b = int(input("Digite o segundo número:"))
div = a / b
if a % b == 0:
    print("O número",a,"é divisível por",b,"e o resultado é:",div)
else:
    print("o número",a,"não é divisível por",b)
