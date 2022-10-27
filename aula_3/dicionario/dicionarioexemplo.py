usuarios = {}
print(usuarios)

usuarios = {
    "chaves" : ["chaves do 8", "24/12/2017", "recep_01"],
    "quico" : ["quico das flores" , "20/12/2017", "raiox_03"]
}
print(usuarios)

usuarios["florinda"] = ["dona florinda", "24/12/2017", "raiox_01"]
print(usuarios)

print("####----####")
print(usuarios.get("quico"))
