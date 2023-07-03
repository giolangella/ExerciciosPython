#Exercício 28: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça ao usuário tentar descobrir qual foi o numero escolhido pelo computador. O programa deve mostrar na tela se o usuário ganhou ou perdeu.
import random
print ("Estou pensando em um número entre 0 e 5, será que você consegue acertar?")
num = random.randint(1,5)
num2 = int(input("Dê o seu palpite: "))
if num2 == num:
    print ('Parabéns! Você acertou!')
else:
    print ('Errado!!! Você perdeu! Eu tinha pensado no número {}.'.format(num))