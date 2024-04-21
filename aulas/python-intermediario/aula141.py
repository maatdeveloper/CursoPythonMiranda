produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritorio'
}

#Dict comprehension
dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor #isinstance verifica o tipo da variavel
    for chave, valor in produto.items()
}
print(dc)

#Set comprehension
sc = {i for i in range(10)}
print(f"\n{sc}")
