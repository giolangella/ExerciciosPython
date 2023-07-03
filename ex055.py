#Exercício 55: Faça um programa que leia o peso de 5 pessoas. No final mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = float('inf')
for c in range(1, 6):
    peso = float(input("Digite o peso da {}ª pessoa: ".format(c)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print("O maior peso digitado foi {}kg e o menor foi {}kg.".format(maior, menor))
