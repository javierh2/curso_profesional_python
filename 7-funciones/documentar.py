# docstring
# las funciones son objetos y todo es documentable
# __doc__ (modulos, clases, metodos, funciones)

def suma(num1, num2):
    """Esta funcion retorna una suma de 2 numeros.

    Argumentos:
    num1 (int)
    num2 (int)


    >>> suma(10, 20)
    30

    >>> suma(100, 200)
    500
    """
    return num1 + num2


print(suma.__doc__)
# print(help(suma))

# se puede testear funciones con la documentacion
