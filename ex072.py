#Exercício 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de 0 até 20. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso.
nuext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
         'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
         'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        num = int(input("Digite um número entre 0 e 20: "))
        if 0 <= num <= 20:
            print(f'Você digitou o número {nuext[num]}.')
            break
        else:
            num = int(input("Número inválido! Digite um número entre 0 e 20: "))
    print("-" * 30)
    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    print("-" * 30)
    while continuar not in "SsNn":
        print("-" * 30)
        continuar = str(input("Não entendi! Deseja continuar? [S/N] ")).strip().upper()[0]
        print("-" * 30)
    if continuar == 'N':
        print("Programa encerrado!")
        break