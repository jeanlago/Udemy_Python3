'''Função que recebe uma matriz e uma linha N, retorna o valor de N '''

def soma_linha_matriz(matriz, N):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == N:
                soma = soma + matriz[i][j]
    return soma


matriz = []

#recebendo dados
for i in range(7):
    matriz_filha = []
    for j in range(6):
        matriz_filha.append(int(input(f'Digite um valor para a posilçao [{i}][{j}]: ')))
    matriz.append(matriz_filha)

#imprimindo a matriz para melhor visibilidade
for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(f'|{matriz[i][j]:^6}|', end=' ')
    print()

N = int(input('Digite a linha que deseja somada: '))

print(soma_linha_matriz(matriz,N-1))
