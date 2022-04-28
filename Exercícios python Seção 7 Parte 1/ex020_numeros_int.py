'''Lendo inteiros em um intervalo 0,50'''

lista =[]
impares = []
for i in range(10):
    X = int(input("digite um número no intervalo (0,50): "))
    lista.append(X)
    if lista[i] % 2 != 0:
        impares.append(lista[i])

for i in range((len(lista) - 1)):
    print(lista[i:(i+2):])

for i in range((len(impares) -1)):
    print(impares[i:(i+2):])
