#Exercício 54: Cria um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
anoatual = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    ano = int(input("Digite o ano de nascimento da pessoa {}: ".format(c)))
    idade = anoatual - ano
    if idade < 21:
        menor +=1
    else:
        maior +=1
print("Dentre os cadastrados existem {} menores de idade e {} maiores de idade".format(menor, maior))
