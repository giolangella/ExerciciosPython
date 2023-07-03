#Exercício 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M e F. Caso esteja errado, peça a digitação novamente até ter um valor correto.
nome = str(input("Digite seu nome: ")).strip().title()
sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()

while sexo not in 'MF':
    sexo = str(input("Sexo inválido! Digite novamente: ")).strip().upper()

print("Cadastro concluído! {} - {}".format(nome, sexo))