def zipper(lista1, lista2):
    intervalo = min(len(lista1), len(lista2))
    return [
        (lista1[i] + lista2[i]) for i in range(intervalo)
    ]


list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
resultado = zipper(list1, list2)
print(resultado)
