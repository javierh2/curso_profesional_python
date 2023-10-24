# metodos con strings

lenguajes = "python php java go c"

# metodo split - lista a partir de string
listado_lenguajes = lenguajes.split()
print(listado_lenguajes)

# metodo join - string a partir de una lista
motores_bdd = ["mysql", "oracle", "mongodb", "sqlite3", "sqlserver"]

string_motores = "-".join(motores_bdd)
print(string_motores)
