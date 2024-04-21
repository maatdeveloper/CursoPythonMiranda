primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite um valor: '))
if primeiro_valor > segundo_valor:
    print(primeiro_valor, 'e maior que', segundo_valor)
elif segundo_valor > primeiro_valor:
    print(segundo_valor, 'e maior que', primeiro_valor)
else:
    print('Os valores sao iguais')
