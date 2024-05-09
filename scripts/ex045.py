
while True:
    try: #vai tentar o codigo abaixo
        peso = float(input('Digite seu peso: '))
        altura = str(input('Digite sua altura(cm): '))

        if len(altura) == 3 and altura.isdigit():
            altura_mt = float(altura)
            altura_mt = altura_mt / 100
            imc = (peso / altura_mt) / altura_mt #formula imc
            imc_tratado = "{:.1f}".format(imc) # formatação do IMC pegando apenas uma casa decimal depois

            if imc <= 18.5: #dentro de um elif deve sempre preceder um if
                resultado = 'Abaixo do peso.'
            
            elif imc > 18.5 and imc <=25:
                resultado = 'Peso ideal. '
            
            elif imc > 25 and imc <= 30:
                resultado = 'Sobrepeso. '

            elif imc > 30 and imc <= 40:
                resultado = 'Obesidade' 

            elif imc > 40:
                resultado = 'Obesidade mórbida. '

            print(f'Seu resultado foi: {imc_tratado}')
            print(f'Situação: {resultado}')

        else:
            print('Digite um número com 3 digitos.')

        reload = input('Reiniciar programa? s/n: ')
        if reload.lower() != 's':
            break

    except ValueError: # se houver um erro do tipo 'ValueError' dentro do bloco try, ele exibe a mensagem abaixo
        print('Digite um número válido.')

        
    