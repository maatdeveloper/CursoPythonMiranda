import os
import time

perguntas = [
    {
        'Pergunta': 'Quanto e 2+2?',
        'Opcoes': ['1', '2', '3', '4'],
        'Resposta': '4'
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

for quest in perguntas:
    x = 0
    os.system('cls')
    for k, v in quest.items():
        if x < 2:
            print(f'{k}: {v}')
        else:
            resp = input('Qual opcao e a correta? ')
            if resp == v:
                print(f'{k}: {v}, PARABENS VOCE ACERTOU!')
            else:
                print(f'{k}: {v}, voce errou...')
        x += 1
    time.sleep(3)
