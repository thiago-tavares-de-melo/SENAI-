#-*- coding: UTF-8 -*-
print("""Olá usuário, digite números e no final imprimirei a soma
dos números pares e dos números ímpares, o programa termina
ao digitar um número maior 1000""")
i = 0
p = 0
while True:
    n = int(input("Digite o número: "))
    if n >= 1000:
        print(f"""Você escolheu sair..
a soma dos números pares é {p}
a soma dos números ímpares é {i}""")
        break
    if n % 2 == 0:
        p = n + p
    elif n % 2 != 0:
        i = n + i
        
        
    
