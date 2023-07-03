#Exercício 75: Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final mostre:
#A - Quantas vezes apareceu o valor 9.
#B - Em que posição foi digitado o primeiro valor 3.
#C - Quais foram os números pares.
num = (int(input("Digite um número: ")),
        int(input("Digite um número: ")),
        int(input("Digite um número: ")),
        int(input("Digite um número: ")))

nove = num.count(9)
print(f"O número 9 apareceu {nove} vezes.")
if 3 in num:
        print(f"O primeiro número 3 foi digitado na {num.index(3) + 1}ª posição.")
else:
        print("O número 3 não foi digitado nenhuma vez.")
print("E os números pares foram: ", end='')
for n in num:
        if n % 2 == 0:
                print(n)



