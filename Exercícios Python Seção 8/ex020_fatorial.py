'''Função para calcular o fatorial de um número'''

def fatorial(NUM):
    FATORIAL = []
    FATOR_PRIMO = 2

    while NUM != 1 and NUM != -1:
        if NUM % FATOR_PRIMO == 0:
            NUM = NUM / FATOR_PRIMO
            FATORIAL.append(FATOR_PRIMO)
        else:
            FATOR_PRIMO = FATOR_PRIMO + 1
    return FATORIAL



NUM = int(input('Digite um valor: '))
if NUM < 1:
    while NUM < 1:
        NUM = int(input('ERRO! Por favor, digite um valor maior que 1: '))

print(f'O fatorial de {NUM} é {fatorial(NUM)}')
