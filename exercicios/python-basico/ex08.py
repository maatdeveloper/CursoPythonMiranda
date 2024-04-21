palavra_secreta = "bolo"
letras_acertadas = ''
tentativas = 0

while True:
    letra = input('DIGITE UMA LETRA: ')

    if len(letra) > 1:
        print('Somente uma letra')
        continue
    
    if letra in palavra_secreta:
        letras_acertadas += letra

    for c in palavra_secreta:
        if c in letras_acertadas:
            print(c, end='')
        else:
            print('*', end='')
    
    print()
    tentativas += 1
    sair = input("DESEJA SAIR? ").lower().startswith('s')
    if sair:
        break
