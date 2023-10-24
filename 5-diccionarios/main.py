# diccionarios, puedan guardar todo tipo de dato y no se rigen por indices como las tuplas y listas
# sino a una llave y cada llave su clave - valor
# una llave puede ser cualquier tipo u objeto inmutable
diccionario = {}
dic_1 = dict()

diccionario = {"total": 55}

dic_1 = {
    "total": 40,
    "descuento": True,
    10: "python",
    (1, 2, 3): "tupla"
}


# el equivalente a un json es un diccionario
# diccionario tipo clase
usuario = {
    "nombre": "Javier",
    "edad": 30,
    "curso": "Curso de Python",
    "skills": {
        "programacion": True,
        "judo": True
    },
    "medallas": ["basico, intermedio"]
}

# se accede al diccionario con []
print(usuario["nombre"])
usuario["nombre"] = "Javo"
print(usuario["nombre"])

user_keys = usuario.keys()      # solo llaves
print(user_keys)
user_values = usuario.values()      # solo valores
print(user_values)
print("\n")
for key, value in usuario.items():      # items de un diccionario
    print(key, value)
print("\n")

calificaciones = usuario.get("calificacion", [])        # se manda una lista vacia para evitar el error
if calificaciones:
    for calificacion in calificaciones:
        print(calificacion)

print(usuario)
