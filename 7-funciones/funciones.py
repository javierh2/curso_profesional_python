# variables dentro de funciones = parametros
# def suma():
#     num1 = int(input("ingresa un num: "))
#     num2 = int(input("ingresa un num: "))
#     result = num1 + num2
#     print(result)


# suma()


def calc(num1, num2):
    # result = num1 + num2
    # print(result)
    # return result
    return num1 + num2, "soy un string en la funcion"     # return devuelve una tupla


num_1 = int(input("ingresa un num: "))
num_2 = int(input("ingresa un num: "))

result, mensaje = calc(num_1, num_2)
print(f"el resultado del calculo es: {result}")
print(mensaje)
