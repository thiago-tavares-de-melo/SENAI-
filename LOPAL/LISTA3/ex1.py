# -*- coding: UTF-8 -*-
print("Olá usuário, digite o raio e a altura de um cilíndro e eu direi o volume")
def babu():
    raio = float(input("Digite o raio do cilíndro: "))
    altura = float(input("Digite a altura: "))
    
    p = 3.14
    v = p * (raio**2) * altura

    print(f"O volume do cilíndro é {v}")

babu()
