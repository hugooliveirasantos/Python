#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com sua idade
#Até 9 anos: Mirim
#Até 14 anos: Infantil
#Até 19 anos: Junior
#Até 20 anos: Sênior
#Acima: Master
while True:
    import datetime
    ano_atual = datetime.datetime.now().year
    ano_nasc = int(input('Digite seu ano de nascimento: '))
    idade = ano_atual - ano_nasc

    if idade <= 9:
        categoria = 'Mirim'

    elif idade > 9 and idade <= 14:
        categoria = 'Infantil'

    elif idade > 14 and idade <= 19:
        categoria = 'Junior'

    elif idade > 19 and idade <= 20:
        categoria = 'Senior'

    elif idade > 20:
        categoria = 'Master'

    print(f'Você tem {idade} anos.')
    print(f'Categoria pertencente: {categoria}')

    reload = str(input('Deseja reiniciar o programa? s/n: '))
    if reload.lower() != 's':
        break

