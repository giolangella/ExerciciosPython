#Exercício 82: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
valores = []
pares = []
impares = []
while True:
    valores.append(int(input("Digite um valor: ")))
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
for i, v in enumerate(valores):
    if v %2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f"Os valores digitados foram {valores}")
print(f"Os valores pares digitados foram {pares}")
print(f"Os valores ímpares digitados foram {impares}")
