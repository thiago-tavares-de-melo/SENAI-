#-*- coding: UTF-8 -*-
print("""Olá usuário, irei receber valores e calcula a soma e a média desses números,
o programa encerra ao receber um número negativo""")
soma = 0
total = 0

while True:
    num = float(input("Digite o valor:"))

    if num > 0:
        soma = soma + 1
        total = total + num

    if num <0:
        media = total / soma
        print(f"Você escolheu sair, o valor total é equivalente à {total} a média dos valores foi de: {media}")
        break 
