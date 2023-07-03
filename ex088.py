#Exercício 88: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
qtde = int(input("Digite a quantidade de jogos que deseja realizar: "))
palpites = []
for c in range(qtde):
    jogo = []
    while len(jogo) < 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    palpites.append(jogo)
print("Palpites gerados: ")
for jogo in palpites:
    print(sorted(jogo))