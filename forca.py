import random 
def jogar(): 
    # INICIALIZAÇÃO DE VARIÁVEIS
    acertou = False
    enforcou = False
    palavras = [] 
    letras_acertadas = []

    # ABERTURA DE ARQUIVO PARA LEITURA
    arquivo = open("animais.txt", "r")
    for linha in arquivo:
        palavras.append(linha.strip())
    #print(palavras)

    # SORTEIO DA PALAVRA SECRETA
    palavra_secreta = random.choice(palavras)
    
    # CRIAÇÃO DO ARRAY SEM AS LETRAS, USANDO _
    for letra in palavra_secreta:
        letras_acertadas.append("_") 

    # CONFIGURAÇÃO DAS TENTATIVAS
    qtde_letras = len(palavra_secreta)
    tentativas = qtde_letras + 1

    # INÍCIO DO JOGO DA FORCA
    print("####### BEM VINDO AO JOGO DA FORCA #######") 
    while (not acertou and not enforcou):
        print("Você tem {} tentativas".format(tentativas))
        print(letras_acertadas)
        index = 0
        chute = input("Digite uma letra\n")
        chute = chute.strip().upper()
        if chute in palavra_secreta.upper():
            for letra in palavra_secreta:
                if chute == letra.upper():
                    letras_acertadas[index] = chute.upper()
                index = index + 1
        else:
            tentativas = tentativas - 1

        if tentativas == 0:
                enforcou = True
        
        if letras_acertadas.count("_") == 0:
            acertou = True
            print("Parabéns você encontrou a palavra secreta!")
            print(letras_acertadas)
        
    print("####### FIM DO JOGO #######")


# EXECUTA O ARQUIVO PELO PRÓPRIO NOME
if (__name__ == "__main__"):
    jogar()

