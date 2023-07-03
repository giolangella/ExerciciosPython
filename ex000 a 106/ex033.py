# Exercício 33: Faça um programa que leia três números que mostre qual é o maior e qual é o menor.
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
# Verificando maior
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
# Verificando menor
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print("O maior número escolhido foi {}".format(maior))
print("O menor número escolhido foi {}".format(menor))
