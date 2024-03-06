import random
max_rand = 10

print("####### BEM VINDO AO JOGO DA ADIVINHAÇÃO #######")
sorteio = random.randint(0, max_rand)
## para criar dificultades: perguntar pro usuário (fácil, médio ou difícil)
## facil = 10 tentatvias (0 - 10)
## medio = 5 tentativas (0 - 50)
## dificil = 3 tentativas (0- 50)

#enquanto (condição for verdadeira)
    #repetirá esses blocos de código
tentativa = 1
limite_tentativas = 3
print("Tente adivinhar o número de 0 a 10, em {} tentativas!".format(limite_tentativas))
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


