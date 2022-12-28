import random


def jogo():

    numero = random.randint(0, 100)

    tentativas = 11
    print(numero)
    while tentativas > 1:

        tentativas = tentativas -1

        print(f'Bem vindo, você tem {tentativas} tentativas para adivinhar o número')
        n_usuario = int(input('Adivinhe o número sorteado: '))

        if n_usuario > numero:
            print('Seu número é maior que o número sorteado, tente novamente!')

        elif n_usuario < numero:
            print('Seu número é menor que o número sorteado, tente novamente!')

        elif n_usuario == numero:
            print('Parabéns você acertou o número!')
            exit(jogo())



jogo()

