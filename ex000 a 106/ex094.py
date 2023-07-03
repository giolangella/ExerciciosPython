#Exercício 94: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
grupo = []
pessoa = {}
soma = media = 0
while True:
    pessoa['Nome'] = str(input("Digite o nome: ")).title().strip()
    pessoa['Sexo'] = str(input("Digite o sexo [M/F]: ")).upper().title().strip()
    if pessoa['Sexo'] not in 'MF':
        pessoa['Sexo'] = str(input("Sexo inválido! Digite o sexo [M/F]: ")).upper().title().strip()
    pessoa['Idade'] = int(input("Digite a idade: "))
    soma += pessoa['Idade']
    grupo.append(pessoa.copy())
    continuar = str(input('Deseja continuar? [S/N] ')).upper().title()
    if continuar not in 'SN':
        continuar = str(input('Opção inválida! Deseja continuar? [S/N] ')).upper().title()
    if continuar == 'N':
        break
media = soma / len(grupo)
print('-' * 40)
print(f"O total de pessoas cadastradas foi de {len(grupo)} pessoas.")
print(f"A média de idade do grupo é de {media:.2f} anos.")
print(f"As mulheres cadastradas foram: ")
for p in grupo:
    if p['Sexo'] == 'F':
        print(p['Nome'])
print('Pessoas acima da idade média:')
for p in grupo:
    if p['Idade'] >= media:
        print(p['Nome'], ' - ', p['Idade'], 'anos.')
