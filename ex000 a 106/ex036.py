"""Exercício 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos meses ele vai pagar.
Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado."""
valorcasa = float(input("Qual o valor da casa que pretende comprar? R$"))
salario = float(input("Qual é a sua renda mensal? R$"))
anos = float(input("Em quantos anos deseja quitar o imóvel? "))
prestacao = valorcasa / (anos * 12)
if prestacao > salario * 0.3:
    print ("O valor da prestação excede 30% do seu salário! Financiamento negado!")
else:
    print ("Empréstimo APROVADO! O valor de cada parcela ficará no valor de {:.2f}".format(prestacao))

