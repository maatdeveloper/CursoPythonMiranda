primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite um valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} e maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} e maior '
        f'do que o {primeiro_valor=}'
    )
