#Exercício 74: Crie um programa que vai gerar 5 numeros aleatorios e colocar em uma tupla. Depois disso, mostre a listagem de numeros gerados e também indique o menor e o maior valores da tupla.
from random import randint
computador = (randint(1,100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
menor = computador[0]
maior = computador[0]
print(f"Os números gerados foram: {computador}")
print(f"O maior número gerado foi {max(computador)}")
print(f"O menor número gerado foi {min(computador)}")