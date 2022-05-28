'''Função para verificar se a matriz é uma matriz identidade'''

from numpy import mat


def mat_identidade(matriz):
    identidade = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)+1):
            if i == j:
                if matriz[i][j] == 1:
                    identidade = identidade + 1
    if identidade == len(matriz):
        return 'Esta é uma matriz identidade.'
    else:
        return 'Esta não é uma matriz identidade.'

matriz = []
for i in range(3):
    matriz_filha = []
    for j in range(3):
        matriz_filha.append(int(input(f'Digite um valor [{i}],[{j}]: ')))
    matriz.append(matriz_filha)

print(mat_identidade(matriz))
