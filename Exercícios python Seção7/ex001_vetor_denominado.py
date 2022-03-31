'''vetor denominado.'''

#letra A
LISTA = [1, 0, 5, -2, -5, 7]
#letra B
print(sum(LISTA[:3]))
#letra C
LISTA.insert(4, 100)
#letra D
VALORES = '\n'.join(str(i) for i in LISTA)
print(VALORES)
print(type(VALORES))
