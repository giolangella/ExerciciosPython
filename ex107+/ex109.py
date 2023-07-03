#Exercício 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import moeda
valor = float(input("Digite um valor: R$"))
taxamenos = float(input("Digite a taxa para diminuir: "))
taxamais = float(input("Digite a taxa para aumentar: "))
print(f"O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}")
print(f"A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}")
print(f"Aumentando {taxamais}% de {moeda.moeda(valor)} fica {moeda.aumentar(valor, taxamais, True)}")
print(f"Diminuindo {taxamenos}% de {moeda.moeda(valor)} fica {moeda.diminuir(valor, taxamenos, True)}")