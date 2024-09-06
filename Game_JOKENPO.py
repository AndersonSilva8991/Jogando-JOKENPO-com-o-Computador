from random import randint

itens = ["PEDRA", "PAPEL", "TESOURA"]
computador = randint(0, 2)
print(''' Suas opções:
[0] - Pedra
[1] - Papel
[2] - Tesoura''')

jogador = int(input("Qual a sua jogada ?: "))
print("O jogador escolheu {}".format(itens[jogador]))
print("Computador escolheu {}".format(itens[computador]))


if computador == 0:
    if jogador == 0:
        print("Empate!")
    elif jogador == 1:
        print("Jogador vence!")
    elif jogador == 2:
        print("Jogador perde!")
    else:
        print("Jogada Inválida!")
elif computador == 1:
    if jogador == 0:
        print("Computador Vence!")
    elif jogador ==1:
        print("Empate!")
    elif jogador == 2:
        print("Jogador Vence!")
    else:
        print("Jogada Inválida!")
elif computador == 2:
    if jogador == 0:
        print("Jogador Vence!")
    elif jogador == 1:
        print("Computador Vence!")
    elif jogador == 2:
        print("Empate!")
    else:
        print("Jogada Inválida")
