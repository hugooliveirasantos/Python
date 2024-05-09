#O primeiro é maior
#O segundo é maior
#Não existe valor maior, os dois são iguais
while True:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite mais um número: '))

    if num1 > num2:
        print(f'{num1} é maior que {num2}. ')
    elif num2 > num1:
        print(f'{num2} é maior que {num1}. ')
    elif num1 == num2:
        print('Os números digitados são iguais. ')
    
    reload = str(input('Deseja reiniciar o programa? s/n: '))
    if reload.lower() != 's':
        break



