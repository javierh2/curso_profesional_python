# son funciones que son utilizados como argumentos para otras funciones que seran las que reciban
# estos argumentos los cuales las llame
# los callbacks son utiles en programas modularizables donde la suplencias son utiles

promedio = lambda *args : sum(args) / len(args)

print(promedio(10, 10, 9, 8, 7))

aprobado = lambda calificacion : calificacion >= 6

print(aprobado(4))


def mostrar_mensaje(promedio, aprobado, *args):
    promedio = promedio(*args)

    if aprobado(promedio):
        print(f"tu resultado {promedio} es aprobado")
    else:
        print(f"tu resultado {promedio} no es aprobable")


mostrar_mensaje(promedio, aprobado, 10, 8, 4, 4, 4)
