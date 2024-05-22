''' Parte teórica
DEF
→ São funções personalizadas, que não existem no Python.
→ Definimos uma função quando for usar várias vezes no código.

'''

''' Exemplo básico de função

def line ():
    print('-'*30)

line()
print('TESTE')
line()

'''

''' Explicação da lógica das funções

def mensagem(msg): #parametro
    print('-'*30)
    print(msg) #printando parametro
    print('-'*30)

mensagem('Olá, Mundo!') #Chamando a função, e dentro do parenteses, armazenando algo no parametro
mensagem('Olá, Hugo!')

'''

''' Definindo função de soma

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B: {s}')
    

soma(b = 4, a = 5)

'''

''' Quantidades de parametros indefinida

def contador (*num):
    for valor in num:
        print(f'{valor}', end='')

def line():
    print('-' * 30)


contador(10, 20, 30, 40, 50)
line()
contador(20, 30, 40, 50)

'''
