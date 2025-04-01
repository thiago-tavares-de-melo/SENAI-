#-*- coding UTF-8 -*-
print("""Olá usuário, irei converter a temperatura de Celsius para Fahrenheit
e vice e versa""")
grau = input("""Digite "C" para converter para Celsius
ou "F" para converter para Fahrenheit:""")
def conv():
    if grau == "C":
        temp_c = float(input("""Digite a temperatura em Fahrenheit para a converção
em Celsius: """))
        c_cont = (tem_c - 32) * (5/9)
        print(f"A temperatura é de {c_cont}° Celsius.")
    if grau == "F":
        temp_f = float(input("""Digite a temperatura em Celsius para a
converção em Fahrenheit: """))
    f_cont = (9/5 * temp_f + 32)
    print(f"A temperatura é de {f_cont}° Fahrenheit.")
conv()
    
        
        
