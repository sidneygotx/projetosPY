def preencherInventario(lista):
    resp="S"
    while resp == "S":
        equipamento=[input("equipamento: "),
                     float(input("valor: ")),
                     int(input("numero serial: ")),
                     input("departamento: ")]
        lista.append(equipamento)
        resp = input("Digite \"s\" para continuar: ").upper()

def exibirInventario(lista):
    for elemento in lista:
        print("nome....: ", elemento[0])
        print("valor....: ", elemento[1])
        print("serial....: ", elemento[2])
        print("departamento....: ", elemento[3])

def localizarPorNome(lista):
    busca=input("\nDigite o nome do equipamento que deseja buscar: ")
    for elemento in lista:
        if busca==elemento[0]:
            print("valor..: ", elemento[1])
            print("serial..: ", elemento[2])

def depreciarPorNome(lista, porc):
    depreciacao=input("\nDigite o nome do equipamento que será depreciado: ")
    for elemento in lista:
        if depreciacao==elemento[0]:
            print("valor antigo: ",elemento[1])
            elemento[1] = elemento[1] * (1-porc/100)
            print("novo valor: ", elemento[1])

def excluirPorSerial(lista):
    serial=int(input("\nDigite o serial do equipamento que será excluido: "))
    for elemento in lista:
        if elemento[2]==serial:
            lista.remove(elemento)
        return "itens excluidos."

def resumirValores(lista):
    valores=[]
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores)>0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))
