equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("equipamentos: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("numero serial: ")))
    departamentos.append(input("departamentos: "))
    resposta = input("digite \"s\" para continuar: ").upper()

for indice in range(0,len(equipamentos)):
    print("\nEquipamento: ", (indice+1))
    print("nome: ", equipamentos[indice])
    print("valor: ", valores[indice])
    print("serial: ", seriais[indice])
    print("departamento: ", departamentos[indice])
