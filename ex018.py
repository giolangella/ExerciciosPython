#Exercício 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import cos, radians, sin, tan
x = int(input('Digite um ângulo: '))
print ('O ângulo {}, tem o seno de {:.3f}, cosseno de {:.3f} e tangente de {:.3f}'.format(x, sin(radians(x)), cos(radians(x)), tan(radians(x))))