'''
Crie um programa que leia vários números inteiros pelo teclado. O programa vai parar quando usuário digitar 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag.)
'''

#Enquanto numero for menor que 999, continuo pedindo entradas. Quando for 999 eu quebro o loop e encerro o programa, mostrando quantos numeros foram digitados. 


contador = 1
numero = 0
soma = 1
while numero < 999:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    else:
        contador += 1
        soma += numero 

print(f'Você digitou {contador} números até chegar em 999')
print(f'A soma de todos os números: {soma}')

