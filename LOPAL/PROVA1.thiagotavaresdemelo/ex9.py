#-*- conding UTF-8 -*-
#a cada 4 anos é um ano bissexto (2022 foi um)
#2 6 0 4 8
print("Olá usuário, digite um ano e eu informarei se ele é bissexto ou não")
ano = int(input("Digite o ano: "))
if ano % 400 == 0:
    print(f"{ano} é um ano bissexto")
elif ano % 400 != 0 and ano % 100 == 0:
    print(f"{ano} não é um ano bissexto")
elif ano % 4 == 0 and ano % 100 != 0:
    print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} é um ano bissexto")
