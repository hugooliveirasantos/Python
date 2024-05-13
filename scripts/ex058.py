'''
Melhore o desafio 28 onde o computador vai pensar em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final, quantos palpites foram necessários para vencer.

Preciso de um contador para contagem de palpite
preciso da lib random choice
'''


'''import random
 
contador = 0
lista = ['1', '2', '3', '4', '5', '6','7','8','9','10']
print('Tente adivinhar qual número, de 1 a 10, o computador escolheu.')
numero = random.choice(lista)


while True: 

    palpite = int(input('Digite seu palpite: '))
    palpite = int(palpite)
    
    if numero == palpite:
        print('Parabéns, você ACERTOU!')
        print(f'Total de tentativas: {contador}')
        break
                              
    else:
        print('Você errou, TENTE NOVAMENTE!')
        print(numero)
        contador +=1
        print(contador)'''

import random
 
contador = 0
lista = ['1', '2', '3', '4', '5', '6','7','8','9','10']
print('Tente adivinhar qual número, de 1 a 10, o computador escolheu.')
numero = random.choice(lista)

while True: 
    palpite = input('Digite seu palpite: ')

    if palpite not in lista:
        print('Digite um número entre 1 e 10. ')
        continue  # Usamos continue para voltar ao início do loop, pedindo outro palpite

    if numero == palpite:
        print('Parabéns, você ACERTOU!')
        print(f'Total de tentativas: {contador}')
        break
                              
    else:
        print('Você errou, TENTE NOVAMENTE!')
        contador += 1
        print(f'Número de tentativas: {contador}')

    print(numero)
    
    

        
    
