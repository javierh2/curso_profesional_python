# la herencia establece relaciones y se puede n cantidad de veces
# clase padre
class Animal():
    def comer(self):
        print("el animal come")

    def dormir(self):
        print("el animal duerme")


class Mascota(Animal):
    pass


class Felino:
    def cazar(self):
        print("el felino caza")


# clase herencia y multiple
class Gato(Mascota, Felino):
    pass


michi = Gato()
michi.cazar()
michi.comer()
michi.dormir()
