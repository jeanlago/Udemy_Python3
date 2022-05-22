'''Função para calcular o fatorial de um número'''

def fatorial(n):
    return n * fatorial(n-1) if n > 1 else 1



NUM = int(input('Digite um valor: '))
if NUM < 1:
    while NUM < 1:
        NUM = int(input('ERRO! Por favor, digite um valor maior que 1: '))

print(f'O fatorial de {NUM} é {fatorial(NUM)}')
