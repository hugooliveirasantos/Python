'''
Faça um programa que leia o peso de cinco pessoas. No final mostre o maior e o menor valor lido.
'''
while True:
    try:
        peso_user = []
        for c in range (5):
            peso = int(input('Digite seu peso: '))
            peso_user.append(int(peso)) #converti a lista para o tipo int

        menor_peso = min(peso_user) #pega o menor valor
        maior_peso = max(peso_user) #pega o maior valor
            
        print(f'Menor peso digitado: {menor_peso}')
        print(f'Maior peso digitado: {maior_peso}')
     
   
    except ValueError:
        print('Houve um erro.')
        break #quebra o loop
    
    reload = input('Reiniciar o programa? (s/n): ').lower()
    if reload != 's':
        break

    

