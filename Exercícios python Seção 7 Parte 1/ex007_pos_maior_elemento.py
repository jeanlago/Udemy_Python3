'''Encontrando o maior elemento e dizendo sua posição na lista'''

lista = []
for i in range(10):
    X = int(input('Digite um número: '))
    lista.append(X)
print(f"o maior valor da lista é {max(lista, key=int)},", end=' ' )
print(f'e sua posição na lista, é: {lista.index(max(lista, key=int))} ')
