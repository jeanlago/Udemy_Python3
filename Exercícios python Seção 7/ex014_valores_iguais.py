'''verificando se há valor igual em lista'''

from collections import defaultdict

lista = []

for i in range(10):
    X = int(input("digite um valor: "))
    lista.append(X)

keys = defaultdict(list);
for key, value in enumerate(lista):
    keys[value].append(key)

for value in keys:
    if len(keys[value]) > 1:
        print(value,keys[value])
