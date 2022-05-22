'''função que recebe um valor e retorna o superfatorial'''


def superfatorial(N):
    from functools import reduce
    from operator import mul
    '''imports para poder multiplicar a lista sem ter que fazer passo a passo'''
    '''função que recebe um valor e retorna o superfatorial'''
    '''superfatorial é definido pelo produto dos N primeiros fatoriais de N'''
    lista = []
    for i in range(N,0,-1):
        for j in range(i,0,-1):
            lista.append(j)
    return reduce(mul,lista, 1)


N= int(input('Digite o número que deseja o superfatorial: '))

print(f'O número superfatorial de {N} é {superfatorial(N)}')
