numero = int(input('Digite um número: '))

def binario(convert):
    #definindo nome da funcao (binario) e atribuindo um argumento (convert). Que será usado mais a frente para receber os valores que sofrerão alterações desta função. Neste caso, ser convertido em um valor binário
    return bin(convert).replace('0b', '')
    #
def octal(convert):
    return oct(convert).replace('0o', '')
def hexadecimal(convert):
    return hex(convert).replace('0x', '')

print(f'Número digitado: {numero}')
print(f'Binário: {binario(numero)} ')
print(f'Octal: {octal(numero)} ')
print(f'Hexadecimal: {hexadecimal(numero)} ')