'''função que retorna a soma de uma matriz[4][4]'''

def soma_mat(matriz):
    soma = 0
    for i in range (len(matriz)):
        for j in range(len(matriz)):
            soma = soma + matriz[i][j]
    return soma


matriz = []

for i in range(4):
    matriz_filha = []
    for j in range(4):
        matriz_filha.append(int(input('Digite um valor: ')))
    matriz.append(matriz_filha)

print(soma_mat(matriz))


