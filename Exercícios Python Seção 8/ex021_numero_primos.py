'''Função cujo irá determinar a quantidade de numeros primos abaixo N'''

def primos_abaixo(NUM):
    PRIMOS = []
    DIVISIVEIS = 0
    i = 0

    while i < NUM:
        for j in range(1, NUM):
            if i > 1 and i % j == 0:
                DIVISIVEIS = DIVISIVEIS + 1
        if DIVISIVEIS == 2:
            PRIMOS.append(i)
        DIVISIVEIS = 0
        i = i + 1
    return PRIMOS


x = int(input('Digite um valor: '))

print(f'A quantidade de numeros primos abaixo de {x} é de {len(primos_abaixo(x))} números.')
