#Exercício 11:Faça um programa que leia a altura e largura de uma parede em metros, calcule a área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m²
a = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede'))
m2 = a * l
print ('Sua parede tem {} m² e serão necessárias {} litros de tinta para printar ela'.format(m2, m2/2))