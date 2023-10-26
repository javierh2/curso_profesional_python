# para que definir/inicializar atributos para un objeto al momento de crearlo
# uso del metodo __init__

class Usuario:
    # todas las clases heredan de la clase object (que posee el metodo init)
    def __init__(self, username, password):
        self.username = username
        self.password = password


user1 = Usuario("Javo", "12345")
user2 = Usuario("Cody", "12345")

# user1.iniciar("javo", "12345")
# user2.iniciar("Cody", "qwerty")

print(user1.__dict__)
print(user2.__dict__)
