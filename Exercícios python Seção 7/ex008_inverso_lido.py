'''Lendo valores e exibindo os mesmos inversamente.'''

LISTA = []
for i in range(6):
    X = int(input("Digite um número: "))
    LISTA.append(X)
print(f"A sequência de números digitados ao contrário, equivale à: {LISTA[::-1]}")