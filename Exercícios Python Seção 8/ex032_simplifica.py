'''função que irá simplificar fraçoes'''

def simplifica(lista=[]):
    for i in range(2, max(lista, key=int,)):
        while (lista[0]/i) // 1 == (lista[0]/i) and (lista[1] / i) // 1 == (lista[1]/i):
            if lista[0] % i == 0 and lista[0] % i == 0:
                lista[0] = lista[0] / i
                lista[1] = lista[1] / i

    return f'{lista[0]} / {lista[1]}'


lista = []
for i in range(2):
    lista.append(int(input('Digite dois valores: ')))

print(simplifica(lista))
