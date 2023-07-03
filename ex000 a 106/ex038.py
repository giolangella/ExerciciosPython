#Exercício 38: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: - O primeiro número é maior, O segundo número é maior, Não existe maior, os dois são iguais.
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if n1 > n2:
    print ("O maior número digitado foi o primeiro, {}.".format(n1))
elif n2 > n1:
    print ("O maior número digitado foi o segundo, {}.".format(n2))
else:
    print ("Os dois valores são iguais!")
