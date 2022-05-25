'''Uma função que retorna os elementos pares e impares '''

def dois_vet(lista, modo):
    '''Recebe uma lista de valores, e se deseja que retorne
    impares, pares ou ambas.'''
    par = []
    impar = []

    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            par.append(lista[i])
        else:
            impar.append(lista[i])

    if modo == 'P' or modo == 'p':
        return f'Pares: {par}'
    elif modo == 'I' or modo == 'i':
        return f'Impares: {impar}'
    else:
        return f'Impares: {impar}, Pares: {par}'



lista = []
for i in range(30):
    lista.append(int(input('Digite um valor: ')))


modo = str(input('Digite I para receber o resultado ímpar, P para receber o resultado par ou A para ambos:'))
if modo != 'i' and modo != 'p' and modo != 'I' and modo != 'P' and modo != 'A' and modo != 'a':
    while modo != 'i' and modo != 'p' and modo != 'I' and modo != 'P' and modo != 'A' and modo != 'a':
        modo = str(input('Erro! Digite I para ímpar, ou P para Par: '))


print(f'Lista dos valores digitados {dois_vet(lista, modo)}')
