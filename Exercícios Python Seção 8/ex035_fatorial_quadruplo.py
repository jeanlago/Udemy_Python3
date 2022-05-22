'''função inteira que recebe um numero inteiro pos e retorna fat quadruplo desse número'''

def fatorial(NUM):
    '''n!, é o produto de todos os inteiros positivos menores ou iguais a n.'''
    lista = []

    for i in range(NUM, 0, -1):
        lista.append(i)

    return lista

def fat_quadruplo(N):
    from functools import reduce
    from operator import mul
    '''imports para poder multiplicar a lista sem ter que fazer passo a passo'''

    dividendo = fatorial(2 * N)
    divisor = fatorial(N)

    return reduce(mul, dividendo, 1) / reduce(mul, divisor, 1)


N = int(input("Digite um valor positivo e inteiro: "))
while N < 1:
    N = int(input("Erro! por favor digite um valor positivo e inteiro: "))

print(f'O fatorial quadrublo do valor {N} equivale à: {fat_quadruplo(N)}')
