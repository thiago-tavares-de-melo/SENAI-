#-*- coding: UTF-8 -*-
print("Olá usuário, irei classificar sua faixa etária de acordo com sua idade")
idade = float(input("Digite sua idade: "))
if idade < 2:
    print("Bebê")
elif idade >= 2 and idade <= 12:
    print("Criança")
elif idade > 12 and idade < 23:
    print("Adolescente")
elif idade >= 23 and idade < 70:
    print("Adulto")
elif idade >= 70:
    print("Idoso")
