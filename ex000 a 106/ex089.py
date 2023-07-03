#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
ficha = list()
while True:
    nome = str(input("Nome do Aluno: "))
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input("Quer continuar? [S/N] "))
    if resp in 'Nn':
        break
print("-" * 50)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print("-" * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print("-" * 35)
    opc = int(input("Deseja ver a nota de qual aluno? (999 interrompe) "))
    if opc == 999:
        print("Programa encerrado!")
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são de {ficha[opc][1]}')
