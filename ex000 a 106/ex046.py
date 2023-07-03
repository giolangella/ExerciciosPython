#Exercício 46: Faça um programa que mostre na tela a contagem regressiva para estouro de fogos de artifício , de 10 a 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print("Feliz ANO NOVO!!!")