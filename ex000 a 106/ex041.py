"""Exercício 41: A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 20 anos: SÊNIOR
Acima: MASTER"""
from datetime import date
atleta = str(input("Digite o nome do atleta: ")).strip().title()
nascimento = int(input("Digite o ano de nascimento do atleta {}: ".format(atleta)))
idade = date.today().year - nascimento
if idade <= 9:
    print("O atelta {} tem {} anos e será inscrito na categoria MIRIM!".format(atleta, idade))
elif idade <= 14:
    print("O atleta {} tem {} anos e será inscrito na categoria INFANTIL!".format(atleta, idade))
elif idade <=19:
    print('O atleta {} tem {} anos e será inscrito na categoria JUNIOR!'.format(atleta, idade))
elif idade <= 25:
    print("O atleta {} tem {} anos e será inscrito na categoria SÊNIOR!". format(atleta, idade))
else:
    print("O atleta {} tem {} anos e será inscrito na categoria MASTER!".format(atleta, idade))

