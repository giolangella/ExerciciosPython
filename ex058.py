#Exercício 58: Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantas tentativas foram feitas.
#MEU CÓDIGO
'''import random
contador = 0
print ("Estou pensando em um número entre 0 e 10, será que você consegue acertar?")
num = random.randint(1,10)
num2 = int(input("Dê o seu palpite: "))
while num2 != num:
    num2 = int(input("Você errou, tente novamente: "))
    contador +=1
print("Você acertou! Pensei no número {}, você precisou de {} tentativas para acertar!".format(num, contador))'''

#CÓDIGO GUANABARA
from random import randint
computador = randint(0, 10)
print("Estou pensando em um número entre 0 e 10, será que você consegue acertar?")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Dê o seu palpite: "))
    palpites +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
print("Você acertou! Pensei no número {}, você precisou de {} tentativas para acertar!".format(computador, palpites))

    