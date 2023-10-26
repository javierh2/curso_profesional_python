# sobre escribir metodos
# la funcion super nos permite acceder a la clase padre inmediate la cual se puede usar para ejecutar sus metodos
# init establece e inicializar los atributos para nuestro objeto
class Animal():
    def comer(self):
        print("el animal come y es la clase que mas come")

    def dormir(self):
        print("el animal duerme")


class Mascota(Animal):

    def comer(self):
        super().comer()
        print("la mascota come mucho por ser Super")


class Felino:
    def cazar(self):
        print("el felino caza")


# clase herencia y multiple
class Gato(Mascota, Felino):
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        super().comer()
        print(f"el {self.nombre} come poco")


michi = Gato("Michi")
print(michi.nombre)
michi.cazar()
michi.comer()
michi.dormir()
