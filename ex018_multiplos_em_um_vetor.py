'''contando multiplos de um inteiro'''

lista =[]
dic = dict
for i in range(10):
    X = int(input('Digite um número: '))
    lista.append(X)

for i in range(10):
    for j in range(11):
        dic = {(f'{lista[i]} * {j}'): (lista[i] * j)}
        print(dic)