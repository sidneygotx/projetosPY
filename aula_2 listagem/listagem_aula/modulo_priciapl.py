from listagem_modulação import *

minhaLista=[]
print("preenchendo")
preencherInventario(minhaLista)
print("Exibindo")
exibirInventario(minhaLista)

print("pesquisando")
localizarPorNome(minhaLista)
print("Alterando")
depreciarPorNome(minhaLista, 20)

print("excluindo")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("resumindo")
resumirValores(minhaLista)
