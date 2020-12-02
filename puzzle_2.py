document = open("number.txt", "r")
# print(document.readlines())
# numeros = [1721, 979, 366, 299, 675, 1456]
numeros = [int(i) for i in document.readlines()]

def main():
    for numero in numeros:
        for numero_2 in numeros:
            for numero_3 in numeros:
                if numero + numero_2 + numero_3 == 2020:
                    return numero * numero_2 * numero_3

if __name__ == "__main__":
    print(main())