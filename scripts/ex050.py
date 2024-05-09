'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''
soma = 0

for i in range(6):
    valor = int(input(f'Digite o {i + 1}° valor: '))
    if valor % 2 == 0:
        soma += valor
       
print(f'Resultado da soma dos pares: {soma}')

        
    


