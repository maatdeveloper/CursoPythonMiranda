import os

lista = ['[i]nserir', '[a]pagar', '[l]istar']
carrinho = []

while True:
    print('Selecione uam opcao: ')
    for c in lista:
        print(c, end=' ')

    item = input(': ').lower()
    if item == 'i':
        nova_compra = input('O que deseja comprar? ')
        carrinho.append(nova_compra)
    elif item == 'a':
        if len(carrinho) < 1:
            print('Seu carrinho esta vazio')
        else:
            retirar = int(input('Qual item deseja tirar do seu carrinho? '))
            carrinho.pop(retirar)
    elif item == 'l':
        if len(carrinho) < 1:
            print('Sua lista esta vazia!')
        else:
            for i, c in enumerate(carrinho):
                print(f'[{i}] {c}')
    
    sair = input('Deseja terminar suas compras? [s]im: ').lower().startswith('s')
    if sair:
        break
    os.system('cls')

#faz dps