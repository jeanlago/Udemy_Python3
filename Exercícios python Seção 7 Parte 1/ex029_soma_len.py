'''recebendo 6 inteiros e dizendo a soma dos impares,
pares e sua quatidade na lista'''

par = []
impar = []
for i in range(6):
    X = int(input('Digite um número: '))
    if X % 2 != 0:
        impar.append(X)
    else:
        par.append(X)
print()
print(f"Dentre os números digitados, os seguintes são pares: {par},",end=' ')
print(f'a soma de todos os números pares é: {sum(par)}, e o tamanho da lista é: {len(par)}')
print()
print(f"Dentre os números digitados, os seguintes são ímpares: {impar},",end=' ')
print(f'a soma de todos os números ímpares é: {sum(impar)}, e o tamanho da lista é: {len(impar)}')
