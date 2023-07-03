#Exercício 13: Faça um algorítmo que leia seu salário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Digite seu salário: R$'))
print ('Seu novo salário com 15% de aumento é R${:.2f}'.format(sal+sal*0.15))