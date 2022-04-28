'''copiando elementos de um vetor'''

vet = []
vet1 = []
vet2 = []

for i in range(10):
    X = int(input("Digite um número: "))
    vet.append(X)

for i in range(10):
    if vet[i] % 2 != 0:
        vet1.append(vet[i])
    else:
        vet2.append(vet[i])
print()
print(f'no vetor 1, tivemos os seguintes elementos utilizados: {vet1}', end=' ')
print(f'no vetor 2, tivemos os seguintes elementos utilizados: {vet2}')