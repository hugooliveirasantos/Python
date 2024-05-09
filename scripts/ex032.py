while True: 
    ano = input('Digite um ano: ')
    if len(ano) == 4 and ano.isdigit():
        ano = int(ano)
        break #quebra o laço quando for verdade a proposição acima
    else:
        print('Digite um ano com exatamente 4 digitos.')
    
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'{ano} é um ano bissexto. ')
else:
    print(f'{ano} não é um ano bissexto. ')
