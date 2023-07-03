#Exercício 45: Crie um programa que faça o computador jogar Jokenpo com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print("-=" * 11)
print("O computador escolheu {}".format(itens[computador]))
print("O jogador escolheu {}".format(itens[jogador]))
print("-=" * 11)
if computador == jogador:
    print("Deu empate!")
elif computador == 0 and jogador == 1 or computador == 1 and jogador == 2 or computador == 2 and jogador == 1:
    print("O jogador VENCEU!!!")
else:
    print("O compuitador VENCEU!!!")




