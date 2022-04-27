'''juntando listas'''

num = []
num2 = []
uniao = []
for i in range(10):
    x = int(input('Digite um número: '))
    num.append(x)
    x = int(input('Digite um número: '))
    num2.append(x)

for i in range(10):
    if num[i] not in uniao:
        uniao.append(num[i])
    if num2[i] not in uniao:
        uniao.append(num2[i])

print(f'a somas dos números repetidos, removendo os iguais é igual à: {uniao}')
