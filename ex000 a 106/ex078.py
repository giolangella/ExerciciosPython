#Exercício 78: Faça um programa que leia 4 valores numéricos e guarde-os em uma lista. No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = list()
for v in range(0, 4):
    valores.append(int(input("Digite um valor: ")))
menor = min(valores)
maior = max(valores)
print(f'Os valores digitados foram {valores}.')
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f"{i}...", end='')
print()
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f"{i}...", end='')