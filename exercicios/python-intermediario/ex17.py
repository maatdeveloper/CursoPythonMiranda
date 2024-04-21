import copy
from pprint import pprint

produtos = [
    {'nome': "Produto 5", 'preco': 10.00},
    {'nome': "Produto 1", 'preco': 22.32},
    {'nome': "Produto 2", 'preco': 10.11},
    {'nome': "Produto 3", 'preco': 105.87},
    {'nome': "Produto 4", 'preco': 69.90}
]

#Exercicio 1
novo_produto = copy.deepcopy(produtos)
novo_produto = [
    {**dic, 'preco': round(dic['preco']*1.1, 2)}
    for dic in novo_produto
]
pprint(novo_produto)
print()

#Exercicio 2
produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome = sorted(
    produtos_ordenados_por_nome,
    key=lambda p: p['nome'], reverse=True
)
pprint(produtos_ordenados_por_nome)
print()

#Exercicio 3
produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco = sorted(
    produtos_ordenados_por_preco,
    key=lambda p: p['preco']
)
pprint(produtos_ordenados_por_preco)