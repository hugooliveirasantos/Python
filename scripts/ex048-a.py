'''
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

Múltiplo de 3 = Números que são multiplicados por 3, portando, quando divididos por 3, o resto da divisão será zero.

Números ímpares, são números que quando divididos por 2, seu resto é 1.
Vou usar um if and para verificar as duas coisas acima.
'''

soma = 0

for i in range(1, 501):
    if (i % 3 == 0) and (i % 2 == 1):
        soma += i

print("A soma dos números ímpares múltiplos de três entre 1 e 500 é:", soma)
