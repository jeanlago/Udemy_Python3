'''recebendo 5 valores não repetidos e calculando'''

X = []
Y = []
for i in range(5):
    x = int(input("Digite um valor: "))
    while x in X:
        x = int(input('Não aceitamos valor repetido, tente outro valor: '))
    X.append(x)

for i in range(5):
    y = int(input('Digite um valor: '))
    while y in Y or y in X:
        y = (int(input('Não aceitamos valor repetido, tente outro valor: ')))
    Y.append(y)

print()
print('SOMA:', end=' ')
for i in range(5):
   print(X[i] + Y[i], end =', ')

print()
print('PRODUTO: ', end=' ')
for i in range(5):
    print(X[i]*Y[i], end=', ')

print()
print('Elementos apenas em X: ', end =' ')
for i in range(5):
    if X[i] not in Y:
        print(X[i], end=', ')

print()
print('Elementos presentes em ambos vetores: ', end=' ')
for i in range(5):
    if X[i] in Y:
        print(X[i], end=', ')
    if Y[i] in X:
        print(Y[i], end=', ')

print()
print('elementos de X: ', end=' ')
for i in range(5):
    print(X[i], end=', ')

print()
print('elementos de Y: ', end=' ')
for i in range(5):
    if Y[i] not in X:
        print(Y[i], end=', ')
