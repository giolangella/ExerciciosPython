#Exercício 37: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher a base de conversão: 1 - binário 2 - octal 3 - hexadecimal
numero = int(input("Digite um número inteiro: "))
(print('''Escolha uma base de conversao para esse número
[1] Binário
[2] Octal
[3] Hexadecimal'''))
convert = int(input("Digite a opção desejada: "))
if convert == 1:
    print("O número {} convertido para binário é {}".format(numero, bin(numero)[2:]))
elif convert == 2:
    print ("O número {} convertido para octal é {}".format(numero, oct(numero)[2:]))
elif convert == 3:
    print("O número {} convertido para hexadecimal é {}".format(numero, hex(numero)[2:]))
else:
    print("Opção inválida! Programa finalizado!")