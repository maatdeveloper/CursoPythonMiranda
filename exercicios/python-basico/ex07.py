while True:
    numero_1 = input("Digite um numero: ")
    numero_2 = input("Digite outro numero: ")
    operacao = input("Digite um operador [+][-][*][/]: ")
    numeros_validos = None

    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        numeros_validos = True
    except: 
        print('Erro! Os numeros nao sao validos')
        continue

    if '+' in operacao or '-' in operacao or '*' in operacao or '/' in operacao:
        if len(operacao) == 1:
            if operacao == '+':
                print(numero_1 + numero_2)
            elif operacao == '-':
                print(numero_1 - numero_2)
            elif operacao == '*':
                print(numero_1 * numero_2)
            elif operacao == '/':
                print(numero_1 / numero_2)
            else:
                print('???')
        else:
            print('Digite somente um operador')
            continue
    else:
        print('Digite um dos operadores possiveis')
        continue

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair:
        break
