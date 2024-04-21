perguntas = [
    {
        'Pergunta': 'Quanto e 2+2?',
        'Opcoes': ['1', '2', '3', '4'],
        'Resposta':'4'
    },
    {
        'Pergunta': 'Quanto e 5*5?',
        'Opcoes': ['25', '55', '10', '51'],
        'Resposta': '25'
    },
    {
        'Pergunta': 'Quanto e 10/2?',
        'Opcoes': ['4', '2', '5', '1'],
        'Resposta': '5'
    }
]

qntd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opcoes']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opcao: ')

    acertou = False
    escolha_int = None
    qnt_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qnt_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    if acertou:
        qntd_acertos += 1
        print('Acertou')
    else:
        print('Errou')
        
    print()

print('Voce acertou', qntd_acertos)
print('de', len(perguntas), 'perguntas.')
