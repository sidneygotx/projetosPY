equipamentos = []
valores = []
seriais = []
departamento = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamentos: "))
    valores.append(float(input("valor: ")))
    seriais.append(int(input("Numero Serial: ")))
    departamento.append(input("departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for indice in range(0,len(equipamentos)):
    print("\nEquipamentos: ", (indice+1))
    print("nome..........: ", equipamentos[indice])
    print("valor ........: ", valores[indice])
    print("Serial........: ", seriais[indice])
    print("Departamento..: ", departamento[indice])
