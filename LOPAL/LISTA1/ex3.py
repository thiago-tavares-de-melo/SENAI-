#-*- coding: UTF-8 -*-
print("Digite dois número inteiros e irei imprimir o maior")
num = int(input("Digite o primero número:"))
num2 = int(input("Digite o segundo número:"))
if num > num2:
    print("O maior número é:",num)
elif num < num2:
    print("O maior número é:",num2)
elif num == num2:
    print("Os números são iguais")
else:
     print("Dígito inválido")
        
