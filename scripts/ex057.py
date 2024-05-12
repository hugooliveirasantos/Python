'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valors M ou F.
Caso esteja errado, peça a digitação novamente, até ter um valor correto.
'''


while True:
        sexo = input('Qual seu sexo (M/F): ').upper()
        if sexo == 'M' or sexo == 'F':
            if sexo == 'M':
                print('Você é do sexo MASCULINO!')
            elif sexo == 'F':
                print('Você é do sexo FEMININO!')
            break
        
        else:
            print('Digite uma opção válida. ')
                    

 


