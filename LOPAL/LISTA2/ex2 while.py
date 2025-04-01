#-*- coding: UTF-8 -*-
print("""Olá usuário, digite valores e no final vou imprimir o menor e o maior
valor digitado, digite um número negativo para parar""")
m = 0
M = 0
while True:
    n = float(input("Digite o valor: "))
    if n < 0:
        print(f"Você escolheu sair, o maior valor é {M} e o menor é {m}")
        break
    elif M == 0 or n > M:
        M = n
    elif m == 0 or n < m:
        m = n
