#-*- coding: UTF-8 -*-
print("""Olá usuário, irei ler a temperatura e imprimir se está
Muito frio, Frio, Agradável, Calor ou Muito quente.""")
temp = float(input("Digite a temperatura atual: "))
if temp <= 15:
    print("Muito frio")
elif temp > 15 and temp <= 23:
    print("Frio")
elif temp > 23 and temp <= 26:
    print("Agradável")
elif temp > 26 and temp <= 30:
    print("Calor")
elif temp > 30:
    print("Muito calor")
