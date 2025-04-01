
#-*- coding: UTF-8 -*-
print("Olá usuário, irei verificar se um número é primo ou não")
def babu(n):
    for v in range(2, n):
        if n % v == 0:
            return f"O número {n} não é primo!"
    return f"O número {n} é primo!"

n = int(input("Digite um número: "))
print(babu(n))
