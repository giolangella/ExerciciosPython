#Exercício 22: Escreva um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiúsculas, todas as letras minusculas, quantas letras sem espaços, quantas letras tem o primeiro nome.
nome = str(input("Digite seu nome completo: ")).strip()
print ('Analisando seu nome...')
print ('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print ('Seu nome em minúsculas é: {}'.format(nome.lower()))
print ('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
#print ('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print ('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
