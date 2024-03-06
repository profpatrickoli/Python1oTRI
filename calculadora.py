
valor_1 = float(input("Digite o primeiro valor: \n"))
valor_2 = float(input("Digite o segundo valor: \n"))

operacao = int(input("Digite a operação desejada:\n 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão \n"))

if operacao == 1 :
    print("A soma é ", valor_1 + valor_2)
elif operacao == 2 :
    print("A subtração é", valor_1 - valor_2)
elif operacao == 3 :
    print("A multiplicação é", valor_1 * valor_2)
elif operacao == 4 :
    print("A divisão é", valor_1 / valor_2)
else :
    print("Operação inválida!")