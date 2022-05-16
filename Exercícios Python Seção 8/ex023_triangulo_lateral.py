'''Função que gera um triângulo lateral de altura 2*n-1 e n altura.'''

def triangulo_lateral(LARGURA):
    ALTURA = 2 * LARGURA - 1
    MEIO = ALTURA//2
    for i in range(1, MEIO+1):
        print('*' * i)

    for j in range(MEIO+1, 1, -1):
        print('*' * j)
    return '*'

LARGURA = int(input("Digite qual a altura do triangulo: "))

print(triangulo_lateral(LARGURA))

