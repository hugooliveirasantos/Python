''' 
 Crie um programa que leia sete anos de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
import datetime 

while True: 
    try:
        ano_nasc = []
        ano_atual = datetime.datetime.now().year
        for c in range(1, 7+1):
            ano_user = input(f'Digite o ano de nascimento {c}: ')
            #verificando comprimento do valor digitado
            if len(ano_user) == 4: 
                #agregando valor da lista para uma variável
                ano_nasc.append(int(ano_user)) 
            else:
                print("Digite em um formato válido.")
                break  # Saia do loop se a entrada não for válida

        # Se todos os anos foram fornecidos corretamente, saia do loop
        if len(ano_nasc) == 7:
            break # Saia do loop se a entrada não for válida

    except ValueError:
        print("Digite em um formato válido.")

ano1, ano2, ano3, ano4, ano5, ano6, ano7 = ano_nasc

for validate in ano1, ano2, ano3, ano4, ano5, ano6, ano7:
    if ano_atual - validate >= 18:
        print(f'{validate}: ATINGIU a maoridade!')
    else:
        print(f'{validate}: NÃO ATINGIU a maioridade.')

