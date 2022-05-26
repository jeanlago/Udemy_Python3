'''Função que calcula a soma elementos abaixo da diagonal principal'''

def abaixo_diagonal(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)+1):
            if i != len(matriz)-1:
                if i == j:
                    soma = soma + matriz[i+1][j]
    return soma

matriz = []

for i in range(3):
    matriz_filha = []
    for j in range(3):
        matriz_filha.append(int(input('Digiteu um valor: ')))
    matriz.append(matriz_filha)


print(f'A soma dos elementos abaixo da diagonal da matriz é: {abaixo_diagonal(matriz)}')
