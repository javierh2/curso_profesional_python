# decoradores -> reducen codigo duplicado, codigo legible, facil de manteter, testear, codigo pythonico
# un decorador es una funcion la cual toma como input una funcion y retorna a su vez una funcion
# a -> funcion principal (decorador)
# b -> funcion de decorar
# c -> funcion decorada
# se usa para extender funcionalidades
# a(b) -> c

def funcion_a(funcion_b):
    def funcion_c():
        # print("desde la funcion decorada")
        # funcion_b()
        print("antes del llamado")
        funcion_b()
        print("despues del llamado")

    return funcion_c


@funcion_a
def saludar():
    print("hola desde una funcion")


saludar()


@funcion_a
def suma():
    print(10 + 30)


suma()
