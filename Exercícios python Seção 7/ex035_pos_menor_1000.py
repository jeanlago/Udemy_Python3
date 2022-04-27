'''lendo positivos menores que 10000, e...'''

Vet = []
Vet2 = []

X = int(input('Digite um número: '))
Y = int(input('Digite um número: '))

if X < 10000 and Y < 10000:
    X = str(X)
    Y = str(Y)
    for i in X:
        Vet.append(int(i))
    Vet.sort()
    for i in Y:
        Vet2.append(int(i))
    print(f'Algarismos do vetor 1: {Vet}')
    print(f'Soma: {sum(Vet) + sum(Vet2)}')
else:
    print('Erro, coloque um valor inteiro menor que 10000.')
