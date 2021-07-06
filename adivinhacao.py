import random

def jogar():
    print("***********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("***********************************")

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("Fácil (1), Médio (2), Difícil (3)")

    dificuldade = int(input("Digite o nível de dificuldade escolhido:"))

    if(dificuldade == 1):
        tentativas = 9
    elif(dificuldade == 2):
        tentativas = 6
    else:
        tentativas = 3

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute = int(input("Digite o seu número: "))

        print("Você digitou", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        acertou   = chute == numero_secreto
        maior     = chute > numero_secreto
        menor     = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()