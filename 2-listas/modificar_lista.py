lista_cursos = ["python", "django", "flask", "mysql", "php", "ruby", "go"]
print(len(lista_cursos))    # len numera los elementos en una lista
lista_cursos.append("javascript")   # agrega un elemento .append
print(lista_cursos)
print(len(lista_cursos))

lista_cursos.insert(0, "linux")     # insert agrega un elementos aunque el 1er parametro es su indice y el 2do lo nuevo
print(lista_cursos)
print(len(lista_cursos))


# extender una lista
lista_cursos_2 = ["aws", "docker", "bigdata"]
lista_cursos.extend(lista_cursos_2)
print(len(lista_cursos))
print(lista_cursos)


# eliminar un elemento de la lista
lista_cursos.remove("bigdata")
print(len(lista_cursos))
print(lista_cursos)

# eliminar un elemento a partir del indice
del lista_cursos[0]
print(len(lista_cursos))
print(lista_cursos)

# limpiar de elementos una lista
lista_cursos.clear()
print(len(lista_cursos))
print(lista_cursos)
