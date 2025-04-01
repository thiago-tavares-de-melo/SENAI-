#-*- coding: UTF-8 -*-
print("""Olá usuário, irei ler o valor do produto e
imprimir o valor de venda para o produto com base no lucro
que você deseja encima do produto""")
preco = float(input("Digite o preço do produto: "))
menor = preco * 0.45
maior = preco * 0.30
lucro_me = (preco * 0.45) + preco
lucro_ma = (preco * 0.30) + preco
if preco <= 20:
    print("O valor para revenda será de: ",lucro_me," tendo",menor,"de lucro")
elif preco > 20:
    print("O valor para revenda será de: ",lucro_ma," tendo",maior,"de lucro")
