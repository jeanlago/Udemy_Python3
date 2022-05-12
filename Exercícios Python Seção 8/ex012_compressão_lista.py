'''função que recebe um numero inteiro maior do que zero e retorna a soma'''
'''de seus algarismos'''

def soma_algarismos(num):
    '''Usando compreensão de lista para dividir um número inteiro em dígitos.'''
    '''As funções str() e int() são usadas para converter um número em uma string e, em seguida, em um inteiro, respectivamente.'''
    lista = [int(a) for a in str(num)]
    return lista

num = int(input('Digite um número inteiro maior do que zero: '))
if num <= 0:
    print('Número inválido.')
    quit()

print(f'O valor {num} corresponde à: {soma_algarismos(num)} {sum(soma_algarismos(num))}')
