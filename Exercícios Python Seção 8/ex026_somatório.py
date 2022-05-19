'''função realizando uma soma acumulada de 0 até o valor N '''


def acumulada(NUM=0):
    SOMA = [17, 18, 16, 21,18]
    for i in range(NUM):
        SOMA.append(int(i))
    return sum(SOMA)

x = int(input("Digite um valor: "))
print(f'O somatório dos números anteriores até o que foi digitado é igual à: {acumulada(x)}.')
