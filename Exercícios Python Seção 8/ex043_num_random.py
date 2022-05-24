'''função vetor de inteiros com numeros aleatórios.'''

def vet_random(quantidade, maximo, minimo):
    '''n resultados aleatórios no intervalo 0-100 '''
    from random import sample
    return sample(range(minimo, maximo), quantidade)



rang= int(input("quantos números devem ser digitados: "))
maximo = int(input('Digite qual o valor máximo: '))
minimo=int(input('Digite o valor minimo: '))

print(vet_random(rang, maximo, minimo))
