'''Calculando produto escalar'''

A = []
B = []
for i in range(3):
    if i == 0:
        a = float(input("Digite um valor para X: "))
        A.append(a)
    if i == 1:
        a = float(input("Digite um valor para Y: "))
        A.append(a)
    if i == 2:
        a = float(input("Digite um valor para Z: "))
        A.append(a)
print()
for i in range(3):
    if i == 0:
        b = float(input('Digite o valor de X: '))
        B.append(b)
    if i == 1:
        b = float(input('Digite o valor de Y: '))
        B.append(b)
    if i == 2:
        b = float(input('Digite o valor de Z: '))
        B.append(b)
SOMA = 0
for i in range(3):
    SOMA = SOMA + (A[i] * B[i])

if SOMA > 0:
    print(f'O produto escalar do vetor {A[0], A[1], A[2]} + o vetor {B[0], B[1], B[2]} é igual à: {SOMA}, e é um ângulo agudo.')
elif SOMA < 0:
    print(f'O produto escalar do vetor {A[0], A[1], A[2]} + o vetor {B[0], B[1], B[2]} é igual à: {SOMA}, e é um ângulo obtuso.')
else:
    print(f'O produto escalar do vetor {A[0], A[1], A[2]} + o vetor {B[0], B[1], B[2]} é igual à: {SOMA}, e é um ângulo reto.')
