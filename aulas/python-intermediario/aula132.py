lista_de_listas_de_inteiros = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 3, 4, 5, 3, 5, 8, 1],
    [8, 4, 5, 3, 7, 4, 2, 1, 6, 1],
    [3, 5, 7, 5, 7, 3, 8, 9, 1, 2],
    [5, 3, 6, 7, 8, 1, 2, 4, 5, 5]
]


def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado


for lista in lista_de_listas_de_inteiros:
    print(
        lista,
        encontra_primeiro_duplicado(lista)
    )
