'''fazendo uma lista até a sexta posição de elementos crescentes, após vira decrescente'''

lista = []
cres = []
decr = []

for i in range(11):
    x = int(input('digite: '))
    lista.append(x)

for i in range(6):
    cres.append(lista[i])
cres.sort()

for i in range(6,11):
    decr.append(str(lista[i]))
decr.sort(reverse = True)

#removendo o [] na hora do print e transformando em lista
cres = " ".join(map(str,cres))
decr = " ".join(map(str,decr))

print(f'{cres} {decr}')
