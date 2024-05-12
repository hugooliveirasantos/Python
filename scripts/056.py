'''

Leia nome, idade e sexo de 4 pessoas.
No final, mostre a média de idade, o nome do homem mais velho
e quantas mulheres tem menos de 20 anos

'''

#criar dicionario

#nome recebe espaço em branco, idade inicia com 0
homem_mais_velho = {'nome': '','idade': 0} 
mulher_menos_20 = 0 #contador
idades = []

for i in range(4):
    #recebendo dados do usuário
    print(f'\nDigite os dados da {i+1}° pessoa: ')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').lower

    #Adicionando idades à lista
    idades.append(int(idade))

    if sexo == 'm' and idade > homem_mais_velho['idade']:
        homem_mais_velho['nome'] = nome
        homem_mais_velho['idade'] = idade

    #Verificando quantas mulheres tem menos de 20
    elif sexo == 'f' and idade < 20: #Se a condição se cumpre, então eu adiciono a variavel.
        mulher_menos_20 += 1 

media = sum(idades) / 5

print(f'Homem mais velho: {homem_mais_velho["nome"]}, com {homem_mais_velho["idade"]} anos.')
print(f'Média de idade {media}')
print(f'Mulheres com menos de 20 anos: {mulher_menos_20}')






