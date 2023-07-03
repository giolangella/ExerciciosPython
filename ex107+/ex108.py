#Exercício 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
import moeda
valor = float(input("Digite um valor: R$"))
taxamenos = float(input("Digite a taxa para diminuir: "))
taxamais = float(input("Digite a taxa para aumentar: "))
print(f"O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}")
print(f"A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}")
print(f"Aumentando {taxamais}% de {moeda.moeda(valor)} fica {moeda.moeda(moeda.aumentar(valor, taxamais))}")
print(f"Diminuindo {taxamenos}% de {moeda.moeda(valor)} fica {moeda.moeda(moeda.diminuir(valor, taxamenos))}")