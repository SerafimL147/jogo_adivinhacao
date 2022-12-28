import random


def jogo():

    numero = random.randint(0, 100)

    tentativas = 1

    while tentativas < 4:

        tentativas = tentativas +1

        n_usuario = int(input('Adivinhe o número sorteado: '))

        if n_usuario > numero:
            print('Seu número é maior que o número sorteado, tente novamente!')

        elif n_usuario < numero:
            print('Seu número é menor que o número sorteado, tente novamente!')

        elif n_usuario == numero:
            print('Parabéns você acertou o número!')


print(jogo())
