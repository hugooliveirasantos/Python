def tipo_triangulo (La,Lb,Lc):
    if (La == Lb) and (Lb == Lc) and (Lc == La):
        return "Equilátero"
    elif (La != Lb) and ( Lb!= Lc) and (Lc != La):
        return "Escaleno"
    else:
        return "Isósceles"
    
def verifica_triangulo(la, lb, lc):
    if (la <= 0) or (lb <=0) or (lc <=0): 
        print('Digite um valor positivo e diferente de 0.')
    else:
        print('Verificando...')
        if (la + lb > lc) and (lb + lc > la) and (la + lc > lb):
           return True
        else:
            return False
def main():
    while True:
        lado_a = float(input('Digite o valor do primeiro lado: '))
        lado_b = float(input('Digite o valor do segundo lado: '))
        lado_c = float(input('Digite o valor do terceiro lado: '))

        if verifica_triangulo (lado_a, lado_b, lado_c):
            print("As retas podem formar um triangulo.")
            tipo = tipo_triangulo(lado_a, lado_b, lado_c)
            print(f"O trângulo é {tipo}")
        else:
            print("As retas não podem formar um triângulo")
           
        continuar = str(input("Deseja continuar? (s/n): ")).lower()
        if continuar != 's':
            break


if __name__ == "__main__":
    main()