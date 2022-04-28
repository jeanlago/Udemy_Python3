'''contando quantas vezes aparece o numero 10 em uma matriz 4x4'''

matriz = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
maior = 0
for i in range(4):
    for j in range(4):
        matriz[i][j] = int(input(f'Digite um valor para a posição ({i}, {j}): '))

for i in range(4):
    for j in range(4):
        if matriz[i][j] > 10:
            maior = maior + 1

print('-=' * 30)
print(f'existe um total de {maior} números maiores que 10 na seguinte matriz.')

#após matriz, está o comando para organizar em 5 casas decimais, para n bagunçar tudo.
for i in range(4):
    for j in range(4):
        print(f'|{matriz[i][j]:^5}|', end='')
    print()
