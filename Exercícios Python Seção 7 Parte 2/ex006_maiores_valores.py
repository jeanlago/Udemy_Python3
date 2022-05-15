'''salvando em uma lista os maiores valores de uma matriz'''

lista = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
maior = [[0], [0], [0], [0]]
for i in range(4):
    for j in range(4):
        lista[i][j] = int(input(f'Digite um valor para a posição ({i+1}, {j+1}): '))

for i in range(4):
    for j in range(4):
        if maior[i][0] < lista[i][j]:
            maior[i][0] = lista[i][j]

print(f'O maior elemento da posição 1 é: {maior[0][0]},',end=' ')
print(f'o maior elemento da posição 2 é: {maior[1][0]},',end=' ')
print(f'o maior elemento da posição 3 é: {maior[2][0]},',end=' ')
print(f'o maior elemento da posição 4 é: {maior[3][0]}.')