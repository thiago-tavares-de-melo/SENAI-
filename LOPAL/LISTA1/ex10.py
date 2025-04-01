#-*- coding: UTF-8 -*-
print("""Olá usuário, digite três valores e eu irei informar qual tipo
de triângulo que esses valores como lados formam""")
v1 = float(input("Digite o primerio valor: "))
v2 = float(input("Digite o segundo valor: "))
v3 = float(input("Digite o terceiro valor: "))
if v1 == v3 and v1 == v2:
    print("O triângulo é equilátero")
elif v1 > v2 + v3 or v2 > v1 + v3 or v3 > v1 + v2:
    print("Essa forma não se caracteriza como um triângulo")
elif v1 == v2 or v1 == v3 or v2 == v3:
    print("O triângulo é isósceles")
elif v1 != v2 and v1!= v3 and v2 != v3:
    print("O triângulo é escaleno")


