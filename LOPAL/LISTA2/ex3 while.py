#-*- coding: UTF-8 -*-
print("""Olá usuário, digite idadesde diversas pessoas e eu imprimirei:
- o total de de pessoas com menos de 21
- o total de pessoas com mais de 50.
(o programa termina ao digitar -99)""")
M = 0
m = 0
while True:
    idade = int(input("Digite a idade: "))
    if idade == -99:
        print(f"""Você escolheu sair..
o número de pessoas com menos de 21 é {m}
o número de pessoas com mais de 50 é {M}""")
        break
    if idade < 21:
        m = m + 1
    elif idade > 50:
        M = M + 1
    
    
