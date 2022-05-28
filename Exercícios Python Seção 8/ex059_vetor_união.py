'''Função que recebe uma matriz e retorna o vetor união'''

def vetor_união(lista, lista2):
    uniao = []
    for i in range(2):
        uniao.append(lista[i])

    for i in range(2):
        uniao.append(lista2[i])

    return uniao

lista = []
lista2 = []

for i in range(5):
    lista.append(int(input(f'Digite um valor para a posição [{i}]: ')))

print()

for i in range(5):
    lista2.append(int(input(f'Digite um valor para a posição [{i}]: ')))

print(vetor_união(lista,lista2))
