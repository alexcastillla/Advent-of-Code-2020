document = open("number.txt", "r")
# print(document.readlines())
# numeros = [1721, 979, 366, 299, 675, 1456]
numeros = [int(i) for i in document.readlines()]

def main():
    for numero in numeros:
        resultado = 2020 - numero
        if resultado in numeros:
            return numero * resultado

if __name__ == "__main__":
    print(main())