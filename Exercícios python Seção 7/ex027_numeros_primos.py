'''Checando se um número é primo.'''

LISTA = []
PRIMOS = []
DIVISIVEIS = 0

for i in range(10):
    Y = int(input("Digite um número inteiro: "))
    LISTA.append(Y)
    for j in range(1,Y+1):
        if Y > 1 and Y % j == 0:
            DIVISIVEIS = DIVISIVEIS + 1
    if DIVISIVEIS == 2:
        PRIMOS.append(Y)
    DIVISIVEIS = 0

print()
print(f'Dos números digitados, apenas os seguintes números são primos: {PRIMOS}, e se encontram nas respectivas posições:', end =' ')

for i in range(len(LISTA)):
    NUM = LISTA[i]
    if NUM in PRIMOS:
        print(f'{LISTA.index(NUM)}', end=' ')
