#-*- coding: UTF-8 -*-
print("""Olá usuário, irei calcular sua média e imprimir se você está
      aprovado, de recuperação ou reprovado""")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
if media < 3:
    print("Sua média foi",media,", você está reprovado")
elif media > 3 and media < 7:
    print("Sua média foi",media,", você está de recuperação")
elif media >= 7 and media <= 10:
    print("Aprovado")
else:
    print("Dígito inválido")
