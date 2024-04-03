import adivinhacao
import forca

jogo = int(input("Digite o jogo desejado: 1 - Adivinhação 2 - Forca"))

if jogo == 1:
    print("Executa adivinhacao")
    adivinhacao.jogar()
else :
    print("Executa forca")
    forca.jogar()