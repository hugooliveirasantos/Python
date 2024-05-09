import random

def jogar_jokenpo(escolha_usuario):
    escolhas = ['pedra', 'papel', 'tesoura']
    escolha_computador = random.choice(escolhas)

    print(f"Você escolheu: {escolha_usuario}")
    print(f"O computador escolheu: {escolha_computador}")

    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
         (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

while True:
    print("\nEscolha: pedra, papel ou tesoura (ou 'sair' para encerrar)")
    escolha = input("Digite sua escolha: ").lower()

    if escolha == 'sair':
        print("Até mais!")
        break
    elif escolha not in ['pedra', 'papel', 'tesoura']:
        print("Escolha inválida. Por favor, tente novamente.")
        continue

    jogar_jokenpo(escolha)
