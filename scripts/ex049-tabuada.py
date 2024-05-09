'''
Crie a tabuada de um numero escolhido pelo usuário
'''
import time
while True:
    numero = int(input('Digite um número: '))
    print('calculando...')
    time.sleep(2)
    for i in range(0,11):
        resultado = numero * i
        print (f'{numero} x {i} = {resultado}')
    
    reload = input('Deseja calcular novamente? (s/n): ').lower()
    if reload != 's':
        quit   
    


