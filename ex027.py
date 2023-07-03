#Exercício 27: Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e último nome separadamente.
nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()
print ('Seu primeiro nome é {}'.format(separa[0]))
print ('Seu último nome é: {}'.format(separa[len(separa)-1]))
