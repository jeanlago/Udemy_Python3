'''alocando todos os zeros à esquerda no vetor'''

from collections import deque
lista = deque()
for i in range(15):
    x = int(input('Digite um valor: '))
    if x != 0:
        lista.appendleft(x)
    else:
        lista.append(x)

print(lista)
