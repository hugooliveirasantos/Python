'''

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

um numero primo só deve ser divisivel por 1 e por ele mesmo, caso ele seja divisivel por mais de 2 numeros, ele nao é primo.


'''


tot = 0
num = int(input('Digite um número: '))
for c in range (1,num+1): 
    '''
    A função range cria um intervalo que vai até, mas não inclui, o número final especificado.Portanto, se quisermos que o loop inclua a variavel num, precisamos fornecer num+1 como o segundo argumento para a função range.
    '''
    if num % c == 0: #se o numero digitado foi divisivel pelo controlador e restar 0
        print(c,'\033[m', end='')
        tot += 1 #caso a condição seja atendida, eu somo +1 ao contador, assim saberei quantas vezes ele foi dividido.
    else:
        print(c,'\033[31m', end='')
    
print(f'\nO número {num} foi dividido {tot} vezes.')
if tot == 2:
    print('Portanto, é um número primo.')
else:
    print('Portanto, não é um número primo.')
   


    



    


