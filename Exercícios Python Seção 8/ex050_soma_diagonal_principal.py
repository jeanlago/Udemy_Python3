'''Função que soma e retorna os elementos da diagonal principal.'''


def diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)+1):
            if i == j:
                soma = soma + matriz[i][j]
    return soma

matriz = []

for i in range(3):
    matriz_filha = []
    for j in range(3):
        matriz_filha.append(int(input('Digite um valor: ')))
    matriz.append(matriz_filha)

print(diagonal_principal(matriz))
