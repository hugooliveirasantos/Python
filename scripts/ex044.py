
while True:
    valor = float(input("Digite o valor do produto: R$"))
    print('Escolha a forma de pagamento: ')
    forma = str(input('[A] à vista dinheiro \n[B] à vista no cartão \n[C] Em até 2x no cartão\n[D] 3x ou mais no cartão\nDigite: '))

    if forma.lower() == 'a':
        desconto = valor * 0.10
        print(f'Você terá um desconto de R$: {desconto}.')

    elif forma.lower() == 'b':
        desconto = valor * 0.05
        print(f'Você terá um desconto de R$: {desconto}.')

    elif forma.lower() == 'c':
        print(f'Você pagará o valor normal de R$: {valor}.')

    elif forma.lower() == 'd':
        juros = valor * 0.20
        print(f'Você terá um juros de R$: {juros}.')

    reload = input('Deseja fazer outra operação:\n[S] Sim\n[N]Não\nDigite: ')
    if reload.lower() != 's':
        break
