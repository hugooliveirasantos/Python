import math
c1 = float(input('Valor do cateto oposto: '))
c2 = float(input('Valor do cateto adjacente: '))
h = math.hypot(c1, c2)
print('O comprimento da hipotenusa é: {}'.format(h))
