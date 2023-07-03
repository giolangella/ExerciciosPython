#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
lista = []
pessoa = []
maior = menor = 0
while True:
    lista.append(str(input("Digite o nome: ")))
    lista.append(float(input("Digite o peso: ")))
    if len(pessoa) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]

    pessoa.append(lista[:])
    lista.clear()
    continuar = str(input("Deseja continuar? [S/N] ")).upper()
    while continuar not in "SsNn":
        print("-" * 30)
        continuar = str(input("Não entendi! Deseja continuar? [S/N] ")).strip().upper()[0]
        print("-" * 30)
    if continuar == 'N':
        print("-" * 30)
        print("Programa encerrado!")
        print("-" * 30)
        break
print("-" * 30)
print(f'Ao todo vc cadastrou {len(pessoa)} pessoas.')
print(f'O maior peso foi de {maior} kgs. Peso de ', end='')
for p in pessoa:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor}kgs. Peso de ', end='')
for p in pessoa:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
