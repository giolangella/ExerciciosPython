#Exercício 25: Crie um programa que leia o nome da pessoa e deiga se tem 'Silva' no nome.
nome = str(input('Digite o seu nome completo: ')).strip().title()
print ('Seu nome tem Silva? {}'.format('Silva' in nome))