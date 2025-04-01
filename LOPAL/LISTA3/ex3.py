#-*- coding: UTF-8 -*-

print("""Olá usuário, irei escfrever a tabuada do número que você
quiser!""")
def babu():
    n = int(input("Digite o número que deseja ver a tabuada: "))
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")
babu()
