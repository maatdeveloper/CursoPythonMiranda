lista = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 3, 4, 5, 3, 5, 8, 1],
    [8, 4, 5, 3, 7, 4, 2, 1, 6, 1],
    [3, 5, 7, 5, 7, 3, 8, 9, 1, 2],
    [5, 3, 6, 7, 8, 1, 2, 4, 5, 5]
]


def duplicata(lista):
    numeros_repetidos = set()
    repetido = -1
    for num in lista:
        if num in numeros_repetidos:
            repetido = num
            break
        numeros_repetidos.add(num)

    return repetido


for c in lista:
    print(c, duplicata(c))
