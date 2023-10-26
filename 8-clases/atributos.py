# atributos de clase - variables dentro de la clase
# atributos de instancia - en py se puede añadir de forma dinamica atributos para los objetos que se almacenan en
# metaatributos __dict__

class Usuario:
    username = "nombre usuario"
    email = "usuario@usuario.com"


# print(Usuario.username)
# print(Usuario.email)

# Usuario.username = "USER1"
# print(Usuario.username)

javo = Usuario()
# verifica si el atrb existe dentro del objeto
print(javo.username)
print(id(Usuario.username))
print(id(javo.username))
# verifica si el atrb existe dentro de la clase - lectura
print(javo.__dict__)     # dict
javo.username = "Javo"
javo.password = "1234"     # añade al objeto un atributo que no existe
print(javo.username)
print(javo.password)
print(javo.__dict__)
print(id(javo.username))
