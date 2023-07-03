from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

cabecalho('SISTEMA CADASTRO v1.0')
while True:
    resposta = menu(['Consultar Cadastros', 'Cadatrar Nova Pessoa', 'Encerrar Programa'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print("Saindo do Sistema")
        break
    else:
        print("Erro! Digite uma opção válida!")
    sleep(2)