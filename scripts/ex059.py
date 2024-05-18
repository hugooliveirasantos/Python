'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] Multiplicar
[3] Maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
while True: 
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    print('Qual operação deseja realizar: ')
    operation = input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair\n')

    if operation == '1':
        soma = n1 + n2
        print(f'O valor da soma é {soma}')
        
    elif operation == '2':
        mult = n1 * n2
        print(f'O resultado da multiplicação é {mult}')

    elif operation == '3':
        if n1 > n2:
            print(f'{n1} é o maior número.')
        elif n1 == n2:
            print('Os números digitados são iguais. ')
        else:
            print(f'{n2} é o maior número.')
    elif operation == '4':
        continue

    elif operation == '5':
        break

