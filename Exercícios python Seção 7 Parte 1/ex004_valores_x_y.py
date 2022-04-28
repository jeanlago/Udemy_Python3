'''vetor de 8 posições com valores x e y quaisquer.'''

lista = []
soma = 0
for i in range(8):
    z = int(input('Digite um número: '))
    lista.append(z)
print(lista)
X = int(input('Digite o valor de X: '))
Y = int(input('Digite o valor de Y: '))
soma = lista[X] + lista[Y]
print(f'A soma dos números correspondentes as posições {X} e {Y} é = {soma}')
