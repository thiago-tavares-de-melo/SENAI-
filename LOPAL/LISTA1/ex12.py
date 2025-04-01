#-*- coding: UTF-8 -*-
print("Olá usuário, digite dois valores e eu os colocarei em ordem crescente")
v1 = int(input("Digitre o primeiro valor: "))
v2 = int(input("Digite o seguhndo valor: "))
if v1 > v2:
    print(f"1°: {v2} 2°:{v1}")
elif v1 < v2:
    print(f"1°: {v1} 2°:{v2}")
else:
    print("Dígito inválido")
