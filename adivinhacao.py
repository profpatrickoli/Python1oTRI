import random

def jogar() :
    print("###### Bem vindo ao jogo de ADIVINHAÇÃO ######")
    ## Atividade 1 - CRIAR DIFICULDADES DIFERENTES:
    ## FÁCIL - 10 TENTATIVAS
    ## MÉDIO - 5 TENTATIVAS
    ## DIFICIL - 3 TENTATIVAS
    dificuldade = int(input("Digite a dificuldade desejada:\n1 - Fácil\n2 - Médio\n3 - Difícil\n"))
    if dificuldade == 1:
        limite_tentativas = 10
        max_rand = 10
    elif dificuldade == 2:
        limite_tentativas = 5
        max_rand = 10
    elif dificuldade == 3:
        limite_tentativas = 5
        max_rand = 100
    else:
        print("Opção inválida, selecionado modo DIFÍCIL")
        max_tentativas = 5
        max_rand = 100
    
    sorteio = random.randint(0, max_rand)
    tentativa = 1
    print("Tente adivinhar o número de 0 a {}, em {} tentativas!".format(max_rand,limite_tentativas))
    while (tentativa <= limite_tentativas) :
        chute = int(input("Digite o valor do seu chute: \n"))

        acertou = chute == sorteio
        maior   = chute  > sorteio
        menor   = chute  < sorteio

        if (acertou):
            print("Parabéns, você acertou!")
            break
        elif (maior):
            print("O número que você digitou é maior")
        elif (menor):
            print("O número que você digitou é menor")
        tentativa = tentativa + 1
        # FIM DO LAÇO

    print("## O número sorteado era: ##", sorteio, "##")

    print("####### FIM DO JOGO #######")


if (__name__ == "__main__"):
    jogar()