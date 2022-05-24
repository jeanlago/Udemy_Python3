'''Função que troca valor de 2 variáveis.'''

def troca(A,B):
    C = B
    B = A
    A = C
    return  f'{A} {B}'

lista =[]
for i in range(2):
    lista.append(float(input('Digite o valor para trocar de posição: ')))

print(f'A troca de posição dos números digitados {lista} fica: {troca(lista[0], lista[1])}')
