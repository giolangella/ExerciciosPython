#Exercício 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar (considere US$1.00 = R$3,27.
n1 = float(input('Quanto você tem na carteira? '))
print ('Com os seus R${} é possível comprar US${:.2f}'.format(n1, n1/3.27))