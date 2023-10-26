# para que definir/inicializar atributos para un objeto al momento de crearlo
# uso del metodo __init__

class Usuario:
    # todas las clases heredan de la clase object (que posee el metodo init)
    def __init__(self):
        print("creando un usuario")


user1 = Usuario()
user2 = Usuario()

# user1.iniciar("javo", "12345")
# user2.iniciar("Cody", "qwerty")

print(user1.__dict__)
print(user2.__dict__)
