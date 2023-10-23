numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, dos, tres, cuatro, *resto_numeros = numeros    # el asterisco denota listas, el resto de valores los guarda en var
uno, dos, tres, cuatro, *_ = numeros    # el _ ignora el restante de datos o un dato
uno, dos, tres, cuatro, *_, nueve, diez = numeros      # el _ ignora el restante de datos pero la "," continua

print(uno)
print(type(uno))
print(dos)
print(tres)
print(cuatro)
print(resto_numeros)
