'''matriz 5x5 com 1 diagonal principal e com 0 os demais elementos'''

mat = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
for i in range(5):
    for j in range(5):
        if i == j:
            mat[i][j] = 1

for i in range(5):
    for j in range(5):
        print(f'|{mat[i][j]:^5}|',end=' ')
    print()
