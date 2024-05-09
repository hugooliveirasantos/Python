#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
#Se ele ainda vai se alistar ao serviço militar
#Se é a hora de se alistar
#Se já passou do tempo de alistamento.
#Seu programa também deve mostrar o tempo que falta ou que passou do prazo.

while True:
    import datetime
    nome = str(input('Digite seu nome: '))
    nasc = int(input('Digite seu ano de nascimento: '))
    sexo = str(input('Você é do sexo masculino ou feminino? (M/F): '))
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - nasc
    alistamento = 18

    if sexo.lower() != 'm':
        print('O alistamento é somente para o sexo masculino. Saindo do programa...')
        exit()

    elif idade == alistamento:
        print('Você deve se alistar ao serviço militar.')

    elif idade < alistamento:
        print(f'{nome} você ainda não tem 18 anos, faltam {alistamento - idade} anos para você se alistar.')

    elif idade > alistamento:
        print(f'{nome} você deveria ter se alistado a {idade - alistamento} anos atrás.')

    reload = str(input('Deseja fazer outra simulação? s/n: '))
    if reload.lower() != 's':
        break
        

    

    

    
