'''Recebendo 6 valores e devolvendo os pares inversamente'''

LISTA = []
for i in range(6):
    X = int(input('digite um número: '))
    if X % 2 == 0:
        LISTA.append(X)

print(f'A sequência inversa de números pares digitados é:{LISTA[::-1]}')