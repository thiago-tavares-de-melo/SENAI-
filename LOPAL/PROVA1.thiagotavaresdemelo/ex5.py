#-*- coding UTF-8 -*-
print("""Olá usuário, irei calcular seu desconto e o valor
final do produto com base na sua idade...
(o desconto é de 10% se idade for superior a 60 anos)""")
v = float(input("Digite o valor da sua compra: "))
i = int(input("Digite a sua idade: "))
p = v / 10
vf = v - p
if i > 60:
    print(f"O desconto foi de {p}, o valor final da compra é de: {vf:.2f}")
