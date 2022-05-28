'''Função que recebe 2 matrizes, e cria uma 3º que é o produto de A e B'''

def produto_matricial(matrizA,matrizB):
    matrizC = []
    for i in range(len(matrizA)):
        for j in range(len(matrizA)):
            matrizC.append(matrizA[i][j] * matrizB[i][j])
    return matrizC

matrizB = []
matrizA = []
n = 2

#recebendo matrizA
for i in range(n):
    matriz_filha = []
    for j in range(n):
        matriz_filha.append(int(input(f'Digite um valor para a matriz(A) posição [{i}][{j}]: ')))
    matrizA.append(matriz_filha)

#recebendo matrizB
for i in range(n):
    matriz_filha = []
    for j in range(n):
        matriz_filha.append(int(input(f'Digite um valor para a matriz(B) posição [{i}][{j}]: ')))
    matrizB.append(matriz_filha)


print(produto_matricial(matrizA, matrizB))
