'''Verificando valores e devolvendo se aparecer mais de 1 vez'''

lista = []
maior = []
iguais = 0
for i in range(5):
    X = int(input('Digite um valor: '))
    lista.append(X)

for i in range(5):
    if lista.count(lista[i]) > 1:
        maior.append(lista[i])
        iguais = iguais + 1
print(f'existem um total de valores iguais: {iguais}, e são os seguintes valores: {maior}')
