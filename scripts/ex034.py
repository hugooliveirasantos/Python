sal = float(input('Digite seu salário: '))
if sal >= 1.250:
    print(f'Seu salário aumentará para: {sal + sal * (10/100)}')
    print('Houve um aumento de 10%')
else:
    print(f'Seu salário aumentará para: {sal + sal *(15/100)}')
    print('Houve um aumento de 15%')
