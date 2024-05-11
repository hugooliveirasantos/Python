''' 
 Crie um programa que leia sete anos de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
import datetime 


ano_nasc = []
ano_atual = datetime.date.year
for c in range (8):
    ano = int(input('Digite seu ano de nascimento: '))
    ano_nasc.append(ano)
    ano1, ano2, ano3, ano4, ano5, ano6, ano7 = ano_nasc

print(ano_atual)

