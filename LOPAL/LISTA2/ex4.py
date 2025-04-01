#-*- coding: UTF-8 -*-
print("Olá usuário, digite um número e eu imprimirei os divisores")
n = int(input("Digite o número: "))

for i in range(1,n):
    if n%i == 0:
        print(i)
