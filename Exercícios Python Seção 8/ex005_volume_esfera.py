'''Calculando o volume de uma esfera.'''
from math import pi

def esfera(Raio):
    '''Calculando o volume.'''
    Volume = 4/3 * pi * (Raio*Raio*Raio)
    return Volume

x = int(input('Digite o valor do Raio: '))

print(f'O valor do volume na esfera é: {esfera(x):.2f} Centímetros Cúbicos')
