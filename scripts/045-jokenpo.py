'''
Faça a máquina jogar jokenpô com você
'''


import random
import time


'''
jogada = ['pedra', 'papel', 'tesoura']

def jokenpo(usuario, maquina):
    if (usuario == 'pedra' and maquina == 'papel') or (usuario == 'papel' and maquina == 'tesoura') or (usuario == 'tesoura' and maquina == 'pedra'):
        return True
    
    else:
        return False

def main ():
    while True:
        print('Faça sua escolha...')
        escolha_usuario = input('Digite pedra, papel ou tesoura: ').lower()
        escolha_maquina = random.choice(jogada)
        if jokenpo(escolha_usuario, escolha_maquina):
            print(escolha_maquina)
            print("Você perdeu!")
        else:
            print(escolha_maquina)
            print ("Você ganhou!")
        reload = input('Quer continuar jogando? (s/n): ').lower()
        if reload != 's':
            break


if __name__ == '__main__':
    main()

'''



while True: 
    jogada = ['pedra', 'papel', 'tesoura']
    escolha_maquina = random.choice(jogada)
    print('Faça sua escolha!')
    escolha_usuario = input('Pedra, papel ou tesoura?: ').lower()
    print("A máquina está escolhendo...")
    time.sleep(3)

    if (escolha_usuario == 'pedra' and escolha_maquina == 'papel') or (escolha_usuario == 'papel' and escolha_maquina == 'tesoura') or (escolha_usuario == 'tesoura' and escolha_maquina == 'pedra'):
        print(f'Escolha da máquina: {escolha_maquina}')
        print('Você perdeu!')

    elif escolha_maquina == escolha_usuario:
        print(f'Escolha da máquina: {escolha_maquina}')
        print('Vocês empataram!')

    else:
        print(f"Escolha da máquina: {escolha_maquina}")
        print('Você ganhou!')

    reload = input('Deseja jogar novamente? (s/n): ').lower()
    if reload != 's':
        break




