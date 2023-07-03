#Exercício 70: Crie um programa que leia o nome e preço de vários produtos. O programa deverá perguntar se o usuário vai continuar e no final:
#A - Qual é o total gasto na compra.
#B - Quantos produtos custam mais de R$1000.
#C - Qual é o nome do produto mais barato.
total = 0
caros = 0
barato = ''
maisbarato = float('Inf')
while True:
    nomeproduto = str(input("Digite o nome do produto: ")).strip().title()
    valor = float(input("Digite o valor do produto: R$"))
    total += valor
    if valor >= 1000:
        caros += 1
    if valor < maisbarato:
        barato = nomeproduto
    print("-" * 30)
    continuar = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    print("-" * 30)
    while continuar not in "SsNn":
        print("-" * 30)
        continuar = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
        print("-" * 30)
    if continuar == 'N':
        break
print (f'O total gasto foi de {total:.2f}')
print (f'{caros} produtos custaram mais de R$1000,00')
print(f"O produto mais barato foi {barato} que custa R${maisbarato:.2f}")