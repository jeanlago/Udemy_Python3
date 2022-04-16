'''Calculando  impares e pares no terceiro vetor'''

A = []
B = []
C = []
for i in range(10):
    a = int(input("Digite um valor: "))
    A.append(a)
    b = int(input("Digite outro valor: "))
    B.append(b)

for i in range(10):
    if A[i] % 2 == 0:
        C.append(A[i])
    if B[i] % 2 != 0:
        C.append(B[i])

print(f'{A}, {B}, {C}')


