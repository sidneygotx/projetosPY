def perguntar():
    return input("o que deseja realizar?\n"+
              "<I> - para inserir um usuário\n"+
              "<P> - Para Pesquisar um usuário\n"+
              "<E> - Para excluir um usuário\n"+
              "<L> - Para Listar um usuário\n").upper()

def inserir(dicionario):
    dicionario[input("Digite o Login: ").upper()] = [input("Digite o nome: ").upper(),
                                                  input("Digite a ultima data de acesso: "),
                                                  input("Qual a última estação acessada: ").upper()]
