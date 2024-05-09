#Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando a mensagem no final de acordo com a média.
#Média abaixo de 5.0 --- Reprovado
#Média entre 5 e 6.9 --- Recuperação
#Média 7.0 ou superior --- Aprovado
while True:
    n1 = float(input('Digite sua primeira nota: '))
    n2 = float(input('Digite sua segunda nota: '))
    media = (n1 + n2) / 2

    if media < 5:
        resultado = 'Reprovado'
    
    elif media >= 5 and media <= 6.9:
        resultado = 'Recuperação'

    elif media >= 7:
        resultado = 'Aprovado'
    
    print(f'Sua média foi: {media}')
    print(f'Resultado: {resultado}')
    
    reload = str(input('Deseja reiniciar o programa? s/n: '))
    if reload.lower() != 's':
        break



