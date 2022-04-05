'''Chegar valores pares dentro de um vetor'''
lista = []
pares = 0
for i in range(10):
    num = int(input("digite um número: "))
    lista.append(num)
for i in range(10):
    if lista[i] % 2 == 0:
        pares = pares + 1
print(f"O vetor possui {pares} números pares.")
