#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
#Ex. Hugo Oliveira Santos
#primeiro = Hugo
#último = Santos


#nome = input('Nome completo: ')
#nome_split = nome.split()
#primeiro_nome = nome_split[0]
#ultimo_nome = nome_split[-1] #o -1 acessa sempre o ultimo ##elemento da lista
#print(f'Primeiro nome: {primeiro_nome}')
#print(f'Último nome: {ultimo_nome}')

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Prazer em te conhecer!')
print(f'Seu primeiro nome é: {nome[0]}')
print(f'Seu último nome é: {nome[-1]}')
