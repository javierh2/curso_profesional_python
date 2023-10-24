elementos = {}
elementos["nombre"] = "Cody"
elementos[(1, 2, 3)] = "la llave es una tupla"
print(elementos)
print(len(elementos))
elementos["nombres"] = "PepeCody"        # si la llave no existe se crea
print(elementos)

registro = {"a": 1, "b": 2, "c": 3, "a": 4}     # toma el ultimo valor asignado, no se permiten las llaves duplicadas
print(registro)
