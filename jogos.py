import forca
import adivinhacao
def escolhe_jogo():
    print("***********************************")
    print("Bem vindo ao jogos!")
    print("***********************************")

    print("Escolha seu jogo!")
    print("Digite 1 para jogar o jogo da forca ou 2 para jogar o jogo da adivinhacao")

    jogos = int(input("Digite o número do jogo que deseja jogar:"))

    if(jogos == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogos == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()