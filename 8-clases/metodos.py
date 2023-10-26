# metodos son funciones dentro
# para que sea un metodo tiene que tener un parametro que haga referencia al objeto perse que llama al metodo (simismo)

class Usuario:
    def iniciar(self, username, password):
        # añadiendo objetos al objeto
        self.username = username
        self.password = password
