def multiplica(*args):
    valores = args
    mult = 1
    for c in valores:
        mult *= c
    return mult

resultado = multiplica(1, 2, 3, 5, 4, 7)
print(f'A multiplicacao de todos os valores e {resultado}')

def parimpar(num):
    if num % 2 == 0:
        return 'Par'
    else:
        return 'Impar'
parouimpar = parimpar(7)
print(parouimpar)
