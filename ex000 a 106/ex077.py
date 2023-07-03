#Exercício 77: Crie um programa que tenha uma tupla com várias palavras. Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.
palavras = (str(input('Digite uma palavra: ')),
            str(input('Digite uma palavra: ')),
            str(input('Digite uma palavra: ')),
            str(input('Digite uma palavra: ')))
for p in palavras:
    print(f'\nNa palavra {p} temos as vogais', end=' ')
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra.lower(), end= " ")