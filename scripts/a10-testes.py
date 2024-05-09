n1 = float(input('Digite sua nota 1: '))
n2 = float(input('Digite sua nota 2: '))
m = (n1 + n2) / 2
if m >=7:
    print('Sua nota {} foi boa. Parabéns!'.format(m))
else:
    print('Sua nota {} foi ruim. Se fodeu!'.format(m))
print('---FIM---')