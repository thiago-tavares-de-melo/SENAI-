#-*- coding: UTF-8 -*-
print("Olá usuário, irei indicar se um número é positivo, negativo ou zero")
n = float(input("Digite o número: "))
if n < 0:
    print(f"O número {n} é negativo")
elif n == 0:
    print(f"O número {n} é 0 kkkk")
elif n > 0:
    print(f"O número {n} é positivo")
else:
    print("Algo deu errado, por favor digite novamente")

