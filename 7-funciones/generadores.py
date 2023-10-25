# un tipo de especial de funcion la cual retorna objetos que se pueden iterar sin que la funcion finalice
def pares():      # generador -> lazy iterador, iterador bajo demanda
    for numero in range(0, 100, 2):
        print("contador")
        # return numero       # return finaliza inmediatamente la ejecucion de la funcion en la primera iteracion
        # print("finalizado")
        yield numero    # yield suspende la ejecucion de la funcion para retornar el objeto y se reunuda desde su estado
        print("reanuda conteo")


# print(pares())
# for par in pares():
#     print(par)


generador = pares()
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print("codigo entre un llamado y otro")
# print(next(generador))
# print(next(generador))

while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print("el generador finalizo el conteo")
        break
