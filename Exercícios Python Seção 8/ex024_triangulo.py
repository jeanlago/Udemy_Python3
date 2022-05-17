'''Função que gera um triângulo de altura e lados n e base 2*n-1.'''

def desenho_triangulo(altura):
    base = 2* altura -1
    caractere = '*'

    for i in range(1 ,base+1):
        '''Se o número for ímpar, digitará o "*" mas com uma formatação do dobro da altura (:^).'''
        if i %2 != 0:
            print(f'{(caractere * i):^{altura*2}}')
    return 'este foi o triângulo gerado.'

num = int(input("Digite um valor: "))

print(desenho_triangulo(num))
