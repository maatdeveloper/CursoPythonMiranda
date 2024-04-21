numero = input('Digite um numero: ')
if numero.isalpha():
    if numero % 2 == 0:
        print(f'{numero} e par')
    else:
        print(f'{numero} e impar')
else:
    print('Digite um numero inteiro')



hora = int(input('Que horas sao? '))
if hora <= 11:
    print('Bom dia')
elif hora <= 17:
    print('Boa tarde')
elif hora <= 24:
    print('Boa noite')
else:
    print('O dia so tem 24 horas')



nome = input('Digite seu nome: ')
if len(nome) <= 4:
    print('Seu nome e curto')
elif len(nome) <= 6:
    print('Seu nome e normal')
elif len(nome) <= 8:
    print('Seu nome grande')
else:
    print('Seu nome e muito grande')
