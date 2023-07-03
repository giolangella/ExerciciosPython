#Exercício 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
x = float(input('Digite o comprimento do cateto oposto: '))
y = float(input('Digite o comprimento do cateto adjacente: '))
print ("Sendo o comprimento do cateto oposto {} e do cateto adj2acente {} o comprimento da hipotenusa será {:.2f}".format(x, y, hypot(x,y)))