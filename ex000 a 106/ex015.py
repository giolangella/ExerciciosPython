#Exercício 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Digite a quantidade de dias alugados: '))
km = float(input('Digite a quantidade de km rodados: '))
pgd = dias * 60
pgkm = km * 0.15
print ('Você utilizou o carro por {} dias e percorreu {}km, totalizando R${:.2f}'.format(dias, km, (pgd+pgkm)))
