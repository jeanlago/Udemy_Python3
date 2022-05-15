'''Função que retorna o maior fator primo de um número.'''


def fat_primo(num):
    valor = num
    fator_primo = 2
    while valor != 1 and valor != -1:
        if valor % fator_primo == 0:
            valor = valor / fator_primo
        else:
            fator_primo = fator_primo + 1
    return f'O maior fator primo de {num} é {fator_primo}'


x = int(input('Digite um valor: '))

print(fat_primo(x))