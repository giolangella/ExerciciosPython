#Exercício 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda
valor = float(input("Digite um valor: R$"))
taxa = float(input("Digite a taxa: "))
print(f"O dobro de R${valor} é R${moeda.dobro(valor)}")
print(f"A metade de R${valor} é R${moeda.metade(valor)}")
print(f"Aumentando {taxa}% de R${moeda.moeda(valor)} fica R${moeda.aumentar(valor, taxa)}")
print(f"Diminuindo {taxa}% de R${moeda.moeda(valor)} fica R${moeda.diminuir(valor, taxa)}")