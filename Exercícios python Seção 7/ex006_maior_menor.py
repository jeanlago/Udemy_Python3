'''maior e menor numero do vetor'''
VET = []
for i in range(10):
    if i > 0:
        x =int(input('digite um número diferente do anterior: '))
    else:
        x = int(input("Digite um número: "))
    VET.append(x)
print(f'O maior elemento da lista é: {max(VET, key=int)}, e o menor elemento é: {min(VET, key=int)}')
