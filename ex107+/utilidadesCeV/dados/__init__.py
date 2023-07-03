def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f"ERRO! {entrada} é um valor inválido!  ")
        else:
            valido = True
            return float(entrada)


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print("ERRO! Digite um valor inteiro válido!")
            continue
        except(KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuário!")
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print("ERRO! Digite um valor inteiro válido!")
            continue
        except(KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuário!")
            return 0
            break
        else:
            return n
