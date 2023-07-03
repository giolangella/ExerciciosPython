#Exercício 85: Crie um programa onde o usuário possa digitar 7 valores numericos e cadastre-os em uma lista unica que mantenha separados valores pares e impares. No final, mostre os valores pares e impares em ordem crescente.
numeros = [[], []]
for c in range(0, 7):
    valor = int(input("Digite um número: "))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

print(f'Os números pares digitados foram {sorted(numeros[0])}')
print(f'Os números ímpares digitados foram {sorted(numeros[1])}')
