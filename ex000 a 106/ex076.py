#Exercício 76: Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequencia. Mo final mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ('Arroz', 2.5, 'Feijao', 3, 'Batata', 5.5, 'Cenoura', 3.2, 'Abacate', 4, 'Maçã', 2.8)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range (0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end = '')
    else:
        print(f'R${produtos[pos]:>4.2f}')
print('-' * 40)
