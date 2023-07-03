#Exercício 91: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
resultados = {}
for jogadores in range(1, 5):
    dado = randint(1, 6)
    resultados[f'Jogador {jogadores}'] = dado
    print(f" O jogador {jogadores} tirou {dado} nos dados")
    sleep(1)
ordem = sorted(resultados.items(), key = itemgetter(1), reverse=True)
print('-' * 40)
print(" ==RANKING DOS JOGADORES==")
for jogador, resultado in ordem:
    print(f'{jogador}: {resultado} pontos')
    sleep(0.5)
    