'''vetor tamanho 50 preenchido com um valor, sendo i a posicao do elemento'''

lista = []
for i in range(50):
    X = (i + 5 * i) % (i + 1)
    lista.append(X)
print(lista)
