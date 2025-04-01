#-*- coding: UTF-8 -*-
print("""Olá usuário, direi se você está aprovado, reporvado por falta
ou reprovado por média""")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
falta = int(input("Digite seu número de faltas: "))
if media < 7.0:
    print("Reprovado por nota")
elif media >= 7.0 and media <= 10:
    print("Aprovado")
elif falta >= 20:
    print("Reprovado por falta")
