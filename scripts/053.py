'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Ex: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA

'''

inverso = ''
frase = str(input('Digite uma frase: ')).strip().upper().split() #pedi para remover espaços descessários, depois para deixar em maiusculas e por fim para dividir a frase em palavras dentro de uma lista
frase_tratada = ''.join(frase) #removi todos os espaços

for c in range(len(frase_tratada) -1, -1, -1): #estou pedindo para o for percorrer a string do final para o começo
    inverso += frase_tratada[c] #esta pegando cada caractere da frase na ordem inversa e armazenando na variavel inverso
if inverso == frase_tratada:
    print(f'{frase_tratada} | {inverso}: Temos um palíndromo!')
else:
    print(f'{frase_tratada} | {inverso}: Não temos um palíndromo.')
