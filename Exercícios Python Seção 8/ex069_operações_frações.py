'''função que faz operações simples de frações'''
import copy

def maximo_divisor(lista):
    mdc = 1
    for i in range(2, max(lista, key=int,)):
        while (lista[0]/i) // 1 == (lista[0]/i) and (lista[1] / i) // 1 == (lista[1]/i):
            if lista[0] % i == 0 and lista[0] % i == 0:
                lista[0] = lista[0] / i
                lista[1] = lista[1] / i
                mdc = mdc * i

    return f'MDC = {mdc}, simplificado: {lista[0]} / {lista[1]}'

def operacoes(lista):
    soma = sum(lista)
    subtracao = lista[0] - lista[1]
    produto = lista[0] * lista[1]
    quociente = lista[0] / lista[1]
    return f'soma: {soma}, subtracao: {subtracao}, produto: {produto}, quociente: {quociente}'


lista = []

for i in range(2):
    lista.append(int(input('Digite dois valores: ')))
lista2 = copy.deepcopy(lista)

print(maximo_divisor(lista))
print(operacoes(lista2))
