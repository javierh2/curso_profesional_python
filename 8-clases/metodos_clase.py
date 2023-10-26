# metodos de instancia y metodos de clase
# metodo de instancia cls hay que decorarlo para que sea de la clase ( cls = self)
class Circulo:
    pi = 3.141592

    @classmethod
    def area(cls, radio):
        return cls.pi * (radio ** 2)


resultado = Circulo.area(14)
print(resultado)
