'''se o valor for negativo atribuir 0'''

lista = []

for i in range(10):
    X = int(input("digite um valor: "))
    if X < 0:
        lista.append(0)
    else:
        lista.append(X)

print(lista)
