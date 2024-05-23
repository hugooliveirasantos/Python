''' TUPLAS - PARTE TEÓRICA
TUPLAS 
• São variáveis compostas (recebe mais de uma informação)
• Os elementos são identificados pelos indices.
• Strings podem ser variáveis compostas, especificamente listas.
• As tuplas são imutáveis.
• Posso ter dados de tipos diferentes.


'''

''' EXEMPLO PRÁTICO



lanches = ('hamburger', 'suco', 'pizza', 'pudim') #tupla // estrutura composta
for lanche in lanches:
    print(lanche)'''

def line():
    print('-'*30)

''' FORMAS DE ACESSAR TUPLAS E SEUS ELEMENTOS

#para mostrar posição
lanches = ('hamburger', 'suco', 'pizza', 'pudim') 
for comida in range(0, len(lanches)):
    print(f'VOU COMER: {lanches[comida]}') 

line()

#não vai mostrar posição
lanches = ('hamburger', 'suco', 'pizza', 'pudim') 
for lanche in lanches:
    print(f'VOU COMER: {lanche}')

line()

#outra forma de mostrar posição
lanches = ('hamburger', 'suco', 'pizza', 'pudim') 
for pos, lanche in enumerate(lanches):
    print(f'POSIÇÃO {pos}: {lanche}')'''

''' ORDENAR TUPLA

lanches = ('hamburger', 'suco', 'pizza', 'pudim') 
print(sorted(lanches)) #ordenação'''

a = ('1', '2', '3')
b = ('4', '5', '6', '7')
c = a + b
print(c)
print(c.index(5))
print(c.count(4))
