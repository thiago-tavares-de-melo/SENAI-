#-*- conding: UTF-8 -*-
import math
print("""Olá usuário, irei calcular a comissão de uma venda com base
no seu valor""")
v = float(input("Digite o valor da venda: "))
m = v/20
M = v/12.333
if v <= 5000:
    print(f"O valor da comissão é de R$:{m:.2f}")
elif v > 5000:
    print(f"O valor da comissão é de R$:{M:.2f}")
