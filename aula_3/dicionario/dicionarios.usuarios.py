from dicionario_funções import *

usuario = {}
opcao = perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuario)
    opcao = perguntar()
