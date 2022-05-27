'''somando a diagonal secundária de uma matriz'''

def diagonal_secundaria(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)+1):
            #testando se i é == numero de colunas-1-j
            if i == len(matriz)-1-j:
                soma = soma + matriz[i][j]
    return soma

matriz = []
for i in range(3):
    matriz_filha = []
    for j in range(3):
        matriz_filha.append(int(input(f'Digite um valor para a posição ({i}, {j}): ')))
    matriz.append(matriz_filha)

print(diagonal_secundaria(matriz))

for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(f'|{matriz[i][j]:^6}|', end=' ')
    print()
