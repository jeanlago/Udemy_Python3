'''preenchendo matriz com o produto do valor da linha e da coluna de cada elemento'''

matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(4):
    for j in range(4):
        matriz[i][j] = (i+1) * (j+1)

for i in range(4):
    for j in range(4):
        print(f'|{matriz[i][j]:^5}|',end='')
    print()
