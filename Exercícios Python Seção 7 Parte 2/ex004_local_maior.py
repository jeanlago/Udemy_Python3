'''lendo uma matriz 4x4 e retornando o maior elemento.'''

lista = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
maior = 0
for i in range(4):
    for j in range(4):
        lista[i][j] = int(input(f'Digite um valor para a posição ({i}, {j}): '))

for i in range(4):
    for j in range(4):
        if lista[i][j] > maior:
            maior = lista[i][j]

print(f'O maior numero encontrado na matriz é: {maior}')
