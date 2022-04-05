'''lendo um conjunto de números reais e armazenando, em seguida, lendo.'''

lista1 = []
lista2 = []
for i in range (10):
    if i == 0:
        x = int(input('Digite um número: '))
    else:
        x = int(input('Digite um número diferente do anterior: '))
    lista1.append(x)
    lista2.append(x*x)

print(lista1)
print(lista2)