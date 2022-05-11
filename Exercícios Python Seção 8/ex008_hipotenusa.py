'''Recebendo 2 valores e calculando a hipotenusa de uma equação.'''
from numpy import sqrt

def hipotenusa(catetoA, CatetoB):
    hipotenusa = sqrt((catetoA**2) + (CatetoB**2))
    return hipotenusa

x = int(input("Digite o valor do cateto A: "))
y = int(input("Digite o valor do cateto B: "))

print(f'O valor da hipotenusa é: {hipotenusa(x,y):.2f}')
