# closures es una funcion la cual puede generar de forma dinamica a otra funcion y esta nueva puede acceder
# a las variables locales a un cuando la primera finalizo

def saludar(username):
    mensaje = f"hola {username}"

    def mostrar_mensaje():
        print(mensaje)
    return mostrar_mensaje


username = "Pepe"
username = "Cody"
respuesta = saludar(username)
username = "Ed"

respuesta()
respuesta()
