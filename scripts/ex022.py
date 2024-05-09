nome_completo = input('Digite seu nome completo: ')
nome_upper = nome_completo.upper()
nome_lower = nome_completo.lower()
nome_sem_espaco = nome_completo.replace(' ', '') #aqui estou pedindo pra substuir os espaços por sem espaços
nome_count = len(nome_completo) #esta contando o comprimento da string
nome_parte = nome_completo.split() #aqui eu dividi o nome completo em partes
nome_first = nome_parte[0] #aqui estou pedindo para atribuir uma váriavel para exibir apenas a primeira parte desse nome, ou seja, a '0'
nome_first_cont =len(nome_first) #aqui estou pedindo pra contar a string dessa nova var
print(f'Uppercase: {nome_upper}')
print(f'LowerCase: {nome_lower}')
print(f'Sem espaço: {nome_sem_espaco}')
print(f'Contagem de {nome_completo}: {nome_count}')
print(f'Contagem de {nome_first}: {nome_first_cont}')



