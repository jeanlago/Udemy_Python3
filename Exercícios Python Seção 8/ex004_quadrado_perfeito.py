'''Função verificando se um número é um quadrado perfeito.'''

from math import sqrt

def quad_perf(x):
    if sqrt(x) % 1 == 0:
        return 'O número digitado é um quadrado perfeito.'
    return 'O número digitado não é um quadrado perfeito.'



y = int(input('Digite um número natural: '))
while y < 0 or type(y) == 'float':
    y = int(input('O número inserido é inválido, por favor digite um número natural: '))

print(quad_perf(y))
