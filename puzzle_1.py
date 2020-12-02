document = open("number.txt", "r")
# print(document.readlines())
# numeros = [1721, 979, 366, 299, 675, 1456]
numeros = [int(i) for i in document.readlines()]

for numero in numeros:
    resultado = 2020 - numero
    if resultado in numeros:
        # print(resultado)
        # # print(numero)
        print(numero * resultado)