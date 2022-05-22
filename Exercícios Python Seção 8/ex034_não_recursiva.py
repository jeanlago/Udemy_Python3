'''função com sequência não recursiva que recebe N impar e retorne o fatorial duplo desse numero.'''
from functools import reduce
from operator import mul

def nao_recursiva(N):
    soma = []
    for i in range(N+1):
        if i % 2 != 0:
            soma.append(i)
    return soma

N = int(input('Digite um valor ímpar: '))
while N % 2 == 0:
    N = int(input('Erro!, Por favor digite um valor ímpar: '))

print(f'O fatorial duplo do valor {N}!! é: ',end='')
print(*nao_recursiva(N), sep= ' * ', end=' = ')
print(reduce(mul, nao_recursiva(N), 1))
