# scope
animal = "leon"     # variable global - funcion, condicion o ciclo


def imprimir_animal():
    global animal
    animal = "ballena"
    # animal = "ballena"  variable local
    tipo = "mamifero"     # variable local

    print(animal)
    print(tipo)
    print(id(animal))


imprimir_animal()
print(animal)
print(id(animal))
