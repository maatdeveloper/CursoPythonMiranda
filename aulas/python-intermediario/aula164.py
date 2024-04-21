# Variaveis livres + nonlocal
def fora(x):
    a = x #Variavel livre
    
    def dentro():
        print(locals())
        return a
    return dentro

dentro1 = fora(10)
dentro2 = fora(20)
print(dentro1())
print(dentro2())

def concatenar(string):
    valor_final = string
    
    def interna(valor_concartenar):
        nonlocal valor_final
        valor_final += valor_concartenar
        return valor_final
    return interna

c = concatenar('a')
print()
print(c('b'))
print(c('c'))
print(c('d'))
