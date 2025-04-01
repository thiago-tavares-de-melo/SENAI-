#-*- coding: UTF-8 -*-
print("""Olá usuário, iriei fazer cálculos simples para você
"+", "-", "x" e "/" """)
def babu():
    cal = input("""Digite qual operação deseja realizar, "+" para adição
"-" para subtração, "x" para multiplicação e "/" para divisão: """)
    v1 = float(input("Digite o primeiro número: "))
    v2 = float(input("Digite o primeiro número: "))
    if cal == "+":
        a = v1 + v2
        print(f"A soma é igual à: {a}")
    if cal == "-":
        s = v1 - v2
        print(f"A subtração é igual à: {s}")
    if cal == "x":
        m = v1 * v2
        print(f"A multiplicação é igual à: {m}")
    if cal == "/":
        d = v1 / v2
        print(f"A divisão é igual à: {d}")
babu()
