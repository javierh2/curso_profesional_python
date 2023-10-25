e = "e"


def funcion_principal():
    a = "a"
    b = "b"

    def funcion_anidada():
        c = "c"

        nonlocal b
        b = "cambio de valor"
        print(a)
        print(b)
        print(id(b))
        print(e)
        print(c)

    funcion_anidada()

    print(b)
    print(id(b))


funcion_principal()

print("\n")


def saludar():
    def mostrar_mensaje():
        print("hola, estamos en el curso de python")

    return mostrar_mensaje


respuesta = saludar()
respuesta()
print(respuesta)
print(type(respuesta))

# las funciones pueden ser asignadas a variables, como argumentos y funciones pueden retornar otras funciones
