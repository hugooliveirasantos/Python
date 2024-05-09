#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra ‘A’ Em que posição ela aparece a primeira vez 
#Em que posição ela aparece a ultima vez


frase = str(input('Digite uma frase: ')).upper() #estou transformando apenas a variavel para upper
print('A letra A aparece {} na frase digitada'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição {}'.format(frase.find('A')+1))#+1 para aparecer da forma 'correta para o usuario'
print('A letra A aparece pela última vez na posição {}'.format(frase.rfind('A')+1)) #o rfind conta do final, da direita.