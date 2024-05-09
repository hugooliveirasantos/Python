while True: #iniciando um loop de repetição. Vai validar as condições até elas serem validadas para o loop ser quebrado
    valor = float(input('Digite o valor a ser financiado: R$'))
    salario = float(input('Digite o seu salário: R$'))
    anos = int(input('Digite em quantos anos pagará o financiamento: '))
    parcela = valor / (anos * 12)

    if parcela > salario * (30/100):
        print('A parcela ultrapassa 30% do seu salário.')
        print(f'R${parcela}')
    else:
        print('Financiamento aprovado. Parabéns!')

    reload = str(input('Deseja fazer outra simulação: digite s ou n: '))
    if reload.lower() != 's':
        break #quando isso for validado, o loop se encerra.