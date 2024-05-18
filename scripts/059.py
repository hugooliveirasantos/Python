'''
Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex: 5! = 5x4x3x2x1 = 120
'''

fatorial = 1 
numero = int(input('Fatorial de: '))

for i in range(1, numero + 1):
        # Multiplica o fatorial pelo número atual do loop
        fatorial *= i
        
print(f'O fatorial de {numero} é: {fatorial}')
#para cada indice dentro do intervalo


'''
Lógica do for: Para caso o usuário digite 5


1° = 1 * 1 
2° = 1 * 2
3° = 2 * 3
4° = 6 * 4
5° = 24 * 5
fatorial = 120

'''