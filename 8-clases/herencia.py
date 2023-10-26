# la herencia establece relaciones y se puede n cantidad de veces
# clase padre
class Mascota:
    def comer(self):
        print("la mascota come")

    def dormir(self):
        print("la mascota duerme")


# clase herencia
class Perro(Mascota):
    pass


class Gato(Mascota):
    pass


duke = Perro()
duke.comer()
duke.dormir()
pepi = Gato()
pepi.comer()
pepi.dormir()