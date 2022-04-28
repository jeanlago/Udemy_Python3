'''lendo 5 valores, em seguida, mostrando o maior, menor e a média'''

lista = []
soma = 0
for i in range(5):
    X = int(input("Digite um valor: "))
    lista.append(X)

for i in range(5):
    soma = soma + lista[i]

media = soma / 5

print(f'A lista contém os seguintes valores: {lista}, seu maior valor é: {len(max(lista, key=int))},', end =' ')
print(f'o seu menor valor é: {min(lista, key=int)} e a média dos valores é: {media}.')
