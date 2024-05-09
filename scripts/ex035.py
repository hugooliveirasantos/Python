while True: 
    try: #vai tentar tudo que esta dentro, se der erro, vai pro except
        a = float(input('Digite o primeiro valor da reta: '))
        b = float(input('Digite o segundo valor da reta: '))
        c = float(input('Digite o terceiro valor da reta: '))

        if (a <= 0) or (b <=0 ) or (c<=0 ):
            
            print('Digite valores positivos e diferentes de 0. ')
        else:
            print('Verificando...')
            if (a + b > c ) and (b + c > a) and (a + c > b):
                print('Com essas medidas, forma-se um triângulo.')

            else:
                print('Com esses valores, não é possível formar um triângulo.')

        continuar = str(input('Deseja calcular novamente? s/n: '))
        if continuar.lower() != 's':
            break
    except: #caso o código acima de qualquer erro de logica, ele cai aqui no print
        print('Algo de errado não está certo.')