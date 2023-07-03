#Exercício 62: Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
print("-=-=-=-=Gerador de PA=-=-=-=-")
pt = int(input("Digite o primeiro termo da PA: "))
rz = int(input("Digite a razão da PA: "))
contador = 1
termo = pt
total = 0
mais = 10
print("Os 10 primeiros termos da PA são:")
while mais != 0:
    total += mais
    while contador <= total:
        print(termo, end= '➝')
        termo += rz
        contador += 1
    print("Pausa!")
    mais = int(input("Quantos termos você quer mostrar a mais? (0 para cancelar)"))
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Progressão finalizada com {} termos mostrados".format(total))
