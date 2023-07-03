#Exercício 99: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(* num):
    cont = maior = 0
    print('Analisando valores passados')
    for valor in num:
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    print(f"Foram digitados {cont} valores.")
    print(f"O maior valor informado foi {maior}.")


maior(1, 3, 7, 9, 22, 4)
