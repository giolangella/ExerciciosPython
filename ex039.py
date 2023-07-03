"""Exercício 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
Se ele ainda vai se alistar ao serviço militar
Se é a hora de se alistar
Se já passou do tempo de se alistar
O seu programa ainda deverá mostrar o campo que falta ou que passou do prazo."""
from datetime import date
nome = str(input("Qual seu nome? ")).strip().title()
idade = int(input("Olá {}, digite seu ano de nascimento: ".format(nome)))
anoatual = date.today().year
if anoatual - idade < 18:
    alistar = 18 - (anoatual - idade)
    print("{}, você precisará se alistar no exército daqui {} anos. No ano de {}".format(nome, alistar, (alistar + anoatual)))
elif anoatual - idade == 18:
    print("{}, você precisará se alistar no exército este ano!".format(nome))
else:
    alistar = (anoatual - idade) - 18
    print("{}, você perdeu o prazo de alistamento no exército! Deveria ter se alistado há {} anos atrás, no ano de {}".format(nome, alistar, (anoatual - alistar)))

