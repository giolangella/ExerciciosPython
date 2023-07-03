#Exercício 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas no final do jogo.
from random import randint
vitoria = 0
print("=-" * 10)
print("VAMOS JOGAR PAR OU ÍMPAR?")
print("=-" * 10)
while True:
    jogador = int(input("Escolha um número: "))
    parimpar = str(input("Par ou Ímpar? [P/I] ")).strip().upper()
    while parimpar not in 'PpIi':
        parimpar = str(input("Par ou Ímpar? [P/I] ")).strip().upper()
    computador = randint(0,10)
    soma = jogador + computador
    resultado = 'P' if soma % 2 == 0 else 'I'

    print(f'Jogador escolheu {jogador}')
    print(f'Computador escolheu {computador}')
    print(f'Resultado: {soma}')

    if resultado == parimpar:
        print("Você venceu!!!")
        vitoria += 1
    else:
        print("Você perdeu!!!")
        break
    print("Vamos jogar novamente...")
    print("-" * 30)
print(f"O total de vitórias consecutivas foi {vitoria}")
