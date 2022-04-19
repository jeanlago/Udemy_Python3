'''Quantidade de numeros negativos e a soma dos numeros positivos
de um vetor'''

pos = []
neg = []
for i in range(10):
    X = float(input("Digite um número real: "))
    if X >= 0:
        pos.append(X)
    else:
        neg.append(X)
print(f'Dentre os números digitados, existem {len(neg)} números negativos', end=" ")
print(f'e a soma de todos os numeros positivos, é igual à:{sum(pos)}')
