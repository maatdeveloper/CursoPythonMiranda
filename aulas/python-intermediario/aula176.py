#Map, Filter, Reduce functions
from functools import partial
from functools import reduce

produtos = [
    {"nome": "Produto 1", "preco": 10},
    {"nome": "Produto 4", "preco": 22.32},
    {"nome": "Produto 2", "preco": 10.11},
    {"nome": "Produto 5", "preco": 105.87},
    {"nome": "Produto 3", "preco": 69.9},
]


def print_iter(iterador):
    print(*list(iterador), sep="\n")
    print()

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


aumenta_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)


def muda_preco_produtos(produto):
    return {
        **produto,
        'preco':aumenta_dez_porcento(
            produto['preco']   
        )
    }
    

#Map
novos_produtos = map(
    muda_preco_produtos,
    produtos
)
print_iter(produtos)
print_iter(novos_produtos)

#Filter
novos_produtos = filter(
    lambda p: p['preco'] > 50,
    produtos
)
print_iter(novos_produtos)

#Reduce
novos_produtos = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0
)
print(round(novos_produtos, 2))
