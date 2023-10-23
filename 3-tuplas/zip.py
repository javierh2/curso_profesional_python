lista = [1, 2, 3, 4, 5]

tupla = (10, 20, 30, 40, 50)

resultado = zip(lista, tupla)   # zip retorna un objeto de tipo zip
resultado = tuple(resultado)
print(resultado)

resultado_2 = zip(lista, tupla)
resultado_2 = list(resultado_2)
print(resultado_2)

# la combinacion exacta de elementos tienen que ser exactas o seran omitidos
