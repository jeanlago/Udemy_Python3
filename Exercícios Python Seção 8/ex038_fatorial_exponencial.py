'''função que recebe um valor e retorna o fatorial exponencial'''

def fat_exponencial(N):
    fat = 0
    for i in range(N+1):
        for j in range(N+1):
            fat = fat + N**((N-j)**(N-j))
    return fat


N= int(input('Digite o número que deseja o fatorial exponencial: '))

print(f'O número superfatorial de {N} é {fat_exponencial(N)}')
