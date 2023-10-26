# metodos son funciones dentro
# para que sea un metodo tiene que tener un parametro que haga referencia al objeto perse que llama al metodo (simismo)

class Usuario:
    def iniciar(self, username, password):
        # añadiendo objetos al objeto
        self.username = username
        self.password = password


user1 = Usuario()
# user1.username = "Javo"
# user1.password = "12345"
user2 = Usuario()
# user2.username = "Cody"
# user2.password = "qwerty"
user1.iniciar("javo", "12345")
user2.iniciar("Cody", "qwerty")

print(user1.__dict__)
print(user2.__dict__)


# NO ES IDEAL ESTO
