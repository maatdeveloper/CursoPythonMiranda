lista = [numero * 2 for numero in range(10)]
print(lista)

sla = lambda x: x * 2
print(sla(2), "\n")

produtos = [
    {'peca':'mouse', 'preco':150},
    {'peca':'teclado', 'preco':200},
    {'peca':'headset', 'preco':150}
]
#Esquerda do for --> map
novos_precos = [
    {**produto, 'preco': produto['preco'] * 0.9}
    if produto['preco'] > 150 else {**produto}
    for produto in produtos
]
print(*novos_precos, sep='\n')

#Direita do for --> filter
listaa = [n for n in range(10) if n < 5]
print(f"\n{listaa}")

#List comprehension com mais de um for
listaaa = [(x,y) for x in range(3) for y in range(3)]
print(f"\n{listaaa}")
