#depreciacao e exclussao
inventario = []
resposta = "S"
while resposta == "S":
    equipamento=[input("Equipamento: "),
                float(input("valor: ")),
                int(input("numero serial: ")),
                input("departamentos: ")]
    inventario.append(equipamento)
    resposta = input("digite \"s\" para continuar: ").upper()

for elemento in inventario:
    print("nome: ", elemento [0])
    print("valor: ", elemento[1])
    print("Serial: ", elemento[2])
    print("departamento: ",elemento[3])

busca=input("\nDigite o nome do equipamento que desenha buscar: ")
for elemento in inventario:
    if busca==elemento[0]:
        print("valor: ", elemento[1])
        print("serial: ", elemento[2])

depreciacao=input("\nDigite o nome do equipamento que será depreciado: ")
for elemento in inventario:
    if depreciacao==elemento[0]:
        print("valor antigo: ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("novo valor: ", elemento[1])

serial=int(input("\nDigite o serial do equipamento que será exluido: "))
for elemento in inventario:
    if elemento[2]==serial:
        inventario.remove(elemento)

for elemento in inventario:
    print("nome: ", elemento[0])
    print("valor: ", elemento[1])
    print("serial: ", elemento[2])
    print("departamento: ", elemento[3])

valores=[]
for elemento in inventario:
    valores.append(elemento[1])
if len(valores)>0:
    print("o equipamento mais caro custa: ", max(valores))
    print("o equipamento mais barato custa: ", min(valores))
    print("o total de equipamentos é de: ", sum(valores))
