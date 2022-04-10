''''Mostrando as posições de maior e menor valor de uma lista'''

lista = []

for i in range(5):
    X = int(input("Digite um valor: "))
    lista.append(X)
print(f"temos a seguinte lista: {lista}")
print(f'O maior valor na lista, se encontra na posição: {lista.index(max(lista, key= int))}.', end = ' ')
print(f'Já o menor valor na lista, se encontra na posição: {lista.index(min(lista, key = int))}.')