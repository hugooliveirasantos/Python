kmh = float(input('Velocidade do carro: '))
if kmh > 80:
    print('Você foi multado!')
    print(f'O valor da sua multa é: R${kmh*7}')
else:
    print('Você não foi multado.')
print('Dirija com cuidado, sempre.')