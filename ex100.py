#Exercício 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep
def sorteio(lista):
    print("Sorteando lista de números:", end=' ')
    for cont in range(0,5):
        n = randint(1, 10)
        lista.append(n)
        print(f"{n}", end=' ')
        sleep(0.5)
    print()

def somapar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'A soma dos números pares da lista é: {soma}')

num = []
sorteio(num)
somapar(num)



