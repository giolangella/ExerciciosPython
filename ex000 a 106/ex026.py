#Exercício 26: Faça um programa que leia uma frase e mostre: quantas vezes aparece a letra 'a', em que posição aparece a primeirca vez e que posição aparece a ultima vez.
frase = str(input('Digite uma frase: ')).strip().lower()
print ('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print ('A primeira letra A aparece na posição {}'.format(frase.find('a')+1))
print ('A última letra A aparece na posição {}'.format(frase.rfind('a')+1))