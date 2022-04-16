'''recebendo 2 valores com 10 int cada, criando um novo vetor e calculando'''

A = []
B = []
C = []
for i in range(10):
    a = int(input("Digite um valor: "))
    A.append(a)
    b = int(input("Digite outro valor: "))
    B.append(b)

for i in range(10):
    C.append(A[i] - B[i])
    print(C)