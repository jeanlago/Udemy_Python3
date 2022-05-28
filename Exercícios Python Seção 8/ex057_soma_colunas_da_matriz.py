'''Função que soma os elementos de uma coluna N'''

def soma_coluna_matriz(matriz,N):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j == N:
                soma = soma + matriz[i][j]
    return soma


matriz = []
for i in range(7):
    matriz_filha = []
    for j in range(6):
        matriz_filha.append(int(input(f'Digite um valor para a posiçãp [{i}][{j}]: ')))
    matriz.append(matriz_filha)

for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(f'|{matriz[i][j]:^6}|', end='')
    print()

N = int(input(f'Digite a coluna a ser somada(0...{len(matriz)-1}): '))

print(soma_coluna_matriz(matriz, N))
