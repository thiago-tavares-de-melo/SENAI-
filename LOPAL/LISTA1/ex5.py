#-*- coding: UTF-8 -*-
print("Olá usuário, irei ler um número inteiro e informar se é multiplo de 3")
num = int(input("Digite o número: "))
if num % 3 == 0:
    print("O número",num,"é múltiplo de 3")
else:
    print("O número",num,"não é múltiplo de 3")
