#-*- coding: UTF-8 -*-
print("""Olá usuário, irei mostrar, com base no seu salário,
o valor da prestação que você pode pagar""")
sal = float(input("Digite o seu salário: "))
prest = float(input("Digite o valor da prestação: "))
porcent = sal * 0.3
if prest > porcent:
    print("Esse valor de prestação é muito alto com base no seu salário")
else:
    print("Parabéns, esse valor de prestação é compatível com seu salário!")
    

