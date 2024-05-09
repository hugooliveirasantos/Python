a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

# verificando se o A é menor
if a < b and a < c:
    menor = a

# verificando se o B é menor
if b < a and b < c:
    menor = b

# verificando se o C é menor
if c < b and c < a:
    menor = c

print(f'O menor número é {menor}')


# verificando se o A é maior
if a > b and a > c:
    maior = a

# verificando se o B é maior
if b > a and b > c:
    maior = b

# verificando se o C é maior
if c > b and c > a:
    maior = c

print(f'O maior número é {maior}')
