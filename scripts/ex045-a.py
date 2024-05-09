import random

def jokenpo(escolha_usuario):
    escolha = ['Pedra', 'Papel', 'Tesoura']
    computador = random.choice(escolha)

    print (f'Você escolheu {escolha_usuario}')
    print (f'O computador escolheu {computador}')

    if escolha_usuario == computador:
        return 'empate'

    elif (escolha_usuario == 'pedra' and computador == 'papel') or \
     (escolha_usuario == 'papel' and computador == 'tesoura') or \
     (escolha_usuario == 'tesoura' and computador == 'pedra'):
        return 'Você perdeu!'
    else:
        return 'Você ganhou!'
    
while True:
    print('Escolha pedra, papel ou tesoura (ou sair para encerrar.)')
    escolha = input('Digite: ').lower
    if escolha == 'sair':
        break
    elif escolha not in ['pedra', 'papel', 'tesoura']:
        print('Digite um valor válido.')
        continue

    jokenpo(escolha)
       