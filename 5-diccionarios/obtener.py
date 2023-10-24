registro = {"a": 1, "b": 2, "c": 3, "d": 4}

valor = registro["d"]      # se puede obtener un valor siempre y cuando exista el mismo
print(valor)

print("z" in registro)

# get - forma segura de obtener una llave

metodo = registro.get("d")      # obtiene el valor de una llave
print(metodo)

non = registro.get("z", "la llave no existe")
print(non)

#  setdefault - obtener el valor de una llave si no existe se crea

llave_e = registro.setdefault("e", 5)
print(registro)
