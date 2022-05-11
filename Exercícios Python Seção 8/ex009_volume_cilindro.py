'''Calculando o volume de um cilindro circular'''

from math import pi
def volume_cilindro(raio, altura):
    volume = 3.1 * ((raio**2) * altura)
    return volume

raio = float(input('Digite o raio do cilindro: '))
alt = float(input('Digite a altura do cilindro: '))

print()
print(f'O volume do cilindro equivale à: {volume_cilindro(raio,alt):.2f}')
