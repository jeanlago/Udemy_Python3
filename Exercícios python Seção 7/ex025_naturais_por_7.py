'''100 primeiros numeros naturais não divisíveis por 7 e que
não terminam em 7'''

lista = []
x = 0

while len(lista) < 100:
    if x % 7 != 0 and x % 10 != 7:
        lista.append(x)
    x += 1
print(lista)
