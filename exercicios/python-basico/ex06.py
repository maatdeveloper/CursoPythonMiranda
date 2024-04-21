frase = input('Digite uma frase: ')
tamanho_frase = len(frase)
x = 0

print('*', end='')
while x < tamanho_frase:
    print(frase[x], end='*')
    x += 1
