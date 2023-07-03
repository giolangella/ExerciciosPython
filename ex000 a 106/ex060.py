#Exercício 60: Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5x4x3x2x1=120
"""from math import factorial
num = int(input("Digite um número para calcular seu fatorial: "))
f = factorial(num)
print("O fatorial de {} é {}".format(num, f))"""

num = int(input("Digite um número para calcular seu fatorial: "))
c = num
f = 1
print("Calculando {}! = ".format(num), end='')
while c > 0:
    print ('{}'.format(c), end=' ')
    print (' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print("{}".format(f))