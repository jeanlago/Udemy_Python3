'''maior e menor numero do vetor'''
VET = []
for i in range(10):
    if i > 0:
        x =int(input('digite um número diferente do anterior: '))
    else:
        x = int(input("Digite um número: "))
    VET.append(x)
MAIOR = 0
for i in range(10):
    if MAIOR < VET[i]:
        MAIOR = VET[i]
        MENOR = MAIOR
for i in range(10):
    if MENOR > VET[i]:
        MENOR = VET[i]
print(f'O maior elemento da lista é: {MAIOR}, e o menor elemento é: {MENOR}')
