import random


def jogo():

    numero = random.randint(0, 100)

    tentativas = 10
    print(numero)
    while tentativas > 0:

        tentativas = tentativas -1

        print('Bem vindo, você tem 10 tentativas para adivinhar o número')
        n_usuario = int(input('Adivinhe o número sorteado: '))

        if n_usuario > numero:
            print(f'Seu número é maior que o número sorteado, tente novamente! Restam {tentativas} tentativas')

        elif n_usuario < numero:
            print(f'Seu número é menor que o número sorteado, tente novamente! Restam {tentativas} tentativas')

        elif n_usuario == numero:
            print('Parabéns você acertou o número!')



jogo()

