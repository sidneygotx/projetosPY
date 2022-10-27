#lista multiplas: inercao e busca
equipamentos = []
valores = []
seriais = []
departamentos = []
respostas = "S"
while respostas == "S":
    equipamentos.append(input("equipamentos: "))
    valores.append(float(input("valor: ")))
    seriais.append(int(input("numero de serial: ")))
    departamentos.append(input("departamentos: "))
    respostas = input("digite \"S\" para continuar: ").upper()

busca=input("\nDigite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(equipamentos)):
    if busca==equipamentos[indice]:
        print("valor: ", valores[indice])
        print("serial: ", seriais[indice])
