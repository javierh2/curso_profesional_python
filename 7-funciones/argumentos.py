# funciones con n cantidad de argumentos
# el * indica que todos los argumentos utilizados al momento de llamar a la funcion van a servir para generar una tupla
# la cual se va asignar al parametro que tengoa el *
def promedio(*listado):
    return sum(listado) / len(listado)


# resultado = promedio([10, 10, 5, 7, 10])      # pasa un listado de 5 argumentos
resultado = promedio(10, 10, 5, 7, 10)
print(resultado)


print("REFACTOR")


def promedio(*args):
    return sum(args) / len(args)


# resultado = promedio([10, 10, 5, 7, 10])      # pasa un listado de 5 argumentos
resultado = promedio(10, 10, 5, 7, 10)
print(resultado)


# args y otros paramentros
print("\n")


def combinacion(p1, p2, *args, p4=500):
    print(p1)
    print(p2)
    print(args)
    print(p4)


combinacion(10, 20, 1, 10, 20, 30, 40, p4=100)

print("\n")
# *kargs


def usuarios(**kwargs):         # pasar diferentes valores , se trabaja con diccionarios
    print(kwargs)
    print(type(kwargs))


usuarios(edu=[10, 10, 8], fer=[10, 9, 8])

# args y kwargs
print("\n")


def union(*args, **kwargs):
    print(args)
    print(kwargs)


union(1, 2, 3, 4, 5, cody=True, curso="python")
