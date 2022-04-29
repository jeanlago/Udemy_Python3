'''Procurando um elemento na matriz'''

matriz = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0]]
encontrei = 0
for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input(f'Digite um valor para a posição ({i}, {j}): '))
print()
X = int(input('Digite o valor a ser buscado na matriz: '))
print()
for i in range(5):
    for j in range(5):
        if X == matriz[i][j]:
            encontrei = 1
            print(f'encontrei o valor {X} na posição ({i}, {j}).')

if encontrei == 0:
    print(f'Não encontrei o elemento {X} na matriz.')
