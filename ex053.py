#Exercício 53: Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print("A frase {} escrita ao contrário é {} e É um palíndromo".format(frase, inverso))
else:
    print("A frase {} escrita ao contrário é {} e NÃO É um palíndromo".format(frase, inverso))