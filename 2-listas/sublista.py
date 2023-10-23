lista_cursos = ["python", "django", "flask", "mysql", "php", "ruby", "go"]

# para generar una sub lista se marca el indice inicial ":" y el indice final dentro de []
# [start:end]
# [start:] -> obtenemos los ultimos elementos
# [:end] -> obtenemos los primeros elementos
# [::2(skip)] -> numero de saltos para generar la sublista
sub_lista = lista_cursos[0::2]
print(sub_lista)
