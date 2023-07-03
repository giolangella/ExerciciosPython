#Exercício 81: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
numeros = []
contador = 0
while True:
    valor = int(input("Digite um valor: "))
    numeros.append(valor)
    contador += 1
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
lista = sorted(numeros, reverse=True)
print(f"Foram digitados {contador} valores na lista.")
print(f'Os números digitados em ordem descrescente são: {lista})')
if 5 in numeros:
    print("O número 5 está na lista.")
else:
    print("O número 5 não está na lista.")

