name = "Ed"
lastname = "Tus"

full_name = name + " " + lastname
print(full_name)

complete = f"{name} {lastname} {10 * 20}"    # interpolacion
print(complete)

another = "Mr. %s %s %s." % (name, lastname, "Jr")
print(another)

format_string = "Mr. {} {} {}.".format(name, lastname, "Second")
print(format_string)
