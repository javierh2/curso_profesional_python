# decoradores -> reducen codigo duplicado, codigo legible, facil de manteter, testear, codigo pythonico
# un decorador es una funcion la cual toma como input una funcion y retorna a su vez una funcion
# a -> funcion principal (decorador)
# b -> funcion de decorar
# c -> funcion decorada
# se usa para extender funcionalidades
# a(b) -> c

def funcion_a(funcion_b):
    def funcion_c(*args, **kwargs):
        # print("desde la funcion decorada")
        # funcion_b()
        print("antes del llamado")
        resultado = funcion_b(*args, **kwargs)
        print("despues del llamado")
        return resultado
    return funcion_c


@funcion_a
def suma(numero1, numero2):
    return numero1 + numero2


resultado = suma(10, 20)
print(resultado)
