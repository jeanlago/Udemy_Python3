'''criando vetores A, B e C, onde C é a intersecção entre A e B'''

NUM = []
NUM2 = []
INTERSECCAO = []
for i in range(10):
    x = int(input("Digite um número: "))
    NUM.append(x)
    x = int(input('Digite um número: '))
    NUM2.append(x)

for i in range(3):
    if NUM[i] in NUM2:
        if NUM[i] not in INTERSECCAO:
            INTERSECCAO.append(NUM[i])
    if NUM2[i] in NUM:
        if NUM2[i] not in INTERSECCAO:
            INTERSECCAO.append(NUM2[i])

print(f'Apenas os seguintes números aparecem em ambos vetores: {INTERSECCAO}')
