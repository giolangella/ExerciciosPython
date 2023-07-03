#Exercício 14: Escreva um programa que converta a temperatura de °C para °F
c = float(input('Digite a temperatura em °C: '))
f = ((9*c)/5)+32
print ('A temperatura {}°C equivale a {:2f}°F'.format(c,f))