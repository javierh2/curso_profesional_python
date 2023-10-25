# ciudadanos de primera clase = funciones pueden ser asignadas a variables, argumentos de otras variables y
# pueden retornar otras funciones

def centigrados_faren(grados):
    return grados * 1.8 + 32


# print(centigrados_faren(30))
# print(centigrados_faren(20))
# print(centigrados_faren(10))

mi_func = centigrados_faren
print(mi_func(30))


print("\n")
# funcion lambda
# lamba siempre hace un retorno del cuerpo de la funcion
# lambda <parametros> : <cuerpo funcion>
# siempre tiene que tener un cuerpo, una expresion a ejecutar
funcion_grados = lambda grados : grados * 1.8 + 32
print(funcion_grados(10))
"""
sin_parametros = lambda : True
parametros_default = lambda p1=10, p2=20, p3=30 : p1 + p2 + p3
asterisco = lambda *args, **kwargs : len(args) + len(kwargs)
"""
