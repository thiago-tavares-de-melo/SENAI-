#-*- coding: UTF-8 -*-
print("Olá usuário, irei informar seu salário líquido")
hora = float(input("Digite quantas horas você trabalhou: "))
sal = hora * 19.50
imp = sal * 0.10
novo_sal = sal - imp
if sal >= 1500.00:
    print("O seu salário líquido é igual a:",novo_sal)
else:
    print("O seu salário líquido é igual a: ",sal)
