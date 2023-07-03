#Exercício 79: Crie um programa que o usuário possa digitar vários valores numericos e cadastre-os em uma lista. Caso o número digitado já exista la dentro, ele não será adicionado. No final, serão exibidos todos os valores unicos, em ordem crescente.
valores = []
while True:

    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor repetido! Não será contabilizado!")

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
print(f'Os números únicos digitados em ordem crescente foram: {sorted(valores)}')