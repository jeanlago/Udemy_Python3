'''recebendo valores diferentes'''

lista = []
for i in range(10):
    x = int(input('Digite um valor: '))
    while x in lista:
        x = int(input('O número já foi digitado, tente outro: '))
    lista.append(x)
print(lista)
