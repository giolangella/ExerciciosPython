#Exercício 80: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
valores = []

for v in range(5):
    valor = int(input("Digite um valor: "))
    if len(valores) == 0:
        valores.append(valor)
        print("Valor inserido na posição 0")
    else:
        posicao = 0
        while posicao < len(valores) and valor > valores[posicao]:
            posicao += 1
        valores.insert(posicao, valor)
        print(f"Valor inserido na posição {posicao}")
print("-" * 30)
print("Lista ordenada:")
for valor in valores:
    print(valor, end=' ')
    print()
print("-" * 30)
