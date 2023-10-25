# contador = 1

# while contador <= 10:
#     print(contador)
#     contador = contador + 1


num = 1234
contador_dig = 0

while num >= 1:
    # contador_dig = contador_dig + 1
    contador_dig += 1
    num = num / 10
else:
    print(contador_dig)
