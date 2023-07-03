#Exercício 24: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palabra 'Santo'
cid = str(input('Digite o nome de uma Cidade: ')).strip().title()
print (cid[:5] == 'Santo')