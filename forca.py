import random

def jogar():
    print("####### BEM VINDO AO JOGO DA FORCA #######")
    palavras = []
    arquivo = open("animais.txt", "r")
    for linha in arquivo:
        palavras.append(linha.strip())
    print(palavras)
    palavra_secreta = random.choice(palavras)

    letras_acertadas = []
    for letra in palavra_secreta:
        letras_acertadas.append("_")

    qtde_letras = len(palavra_secreta)
    tentativas = qtde_letras + 1
    acertou = False
    enforcou = False
    while (not acertou and not enforcou):
        
        print("Você tem {} tentativas".format(tentativas))
        print(letras_acertadas)
        index = 0
        chute = input("Digite uma letra\n")
        chute = chute.strip()
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_acertadas[index] = chute.upper()
            index = index + 1
        
        if letras_acertadas.count("_") == 0:
            acertou = True
            print("Parabéns você encontrou a palavra secreta!")
            print(letras_acertadas)
        

        tentativas = tentativas - 1
        if tentativas == 0:
            enforcou = True
        
        ##print("executando forca", index)
    print("####### FIM DO JOGO #######")


if (__name__ == "__main__"):
    jogar()

