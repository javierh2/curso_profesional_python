def area_circulo(radio, pi=3.14):    # valor default para parametros
    return pi * (radio ** 2)


result = area_circulo(10, 3.141592)       # si la funcion recibe un argumento como valor es usado dicho valor
print(result)
