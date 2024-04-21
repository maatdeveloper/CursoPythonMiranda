nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if len(nome) > 0 and len(idade) > 0:
    print(f'Seu nome e {nome}')
    print(f'Seu nome invertido e {nome[-1::-1]}')
    print(f'Seu nome contem espacos? {" " in nome}')
    print(f'Seu nome contem {len(nome)}')
    print(f'A primeira letra do seu nome e: {nome[0]}')
    print(f'A ultima letra do seu nome e: {nome[-1]}')
else:
    print('Preencha todos os campos')
