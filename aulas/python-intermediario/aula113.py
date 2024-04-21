def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
multiplicacao = multiplicar(10, 2, 3, 5, 4)
print(multiplicacao)

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} e par'
    else:
        return f'{numero} e impar'

print(par_impar(18))
