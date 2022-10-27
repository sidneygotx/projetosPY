usuario ={}
emails = ["xptp@xyz.com", "xkd@phd.com"]

tupla = list(enumerate(emails))

for chave in range(0, len(tupla)):
    print("email: ", tupla[chave][1])
    usuario[tupla[chave]]=[input("Digite o nome: "), input("digite o nível")]

for chave, dado in usuario.items():
    print("usuario: ", chave[0])
    print("email: ", chave[1])
    print("nome: ",dado[0])
    print("nível: ", dado[1])
