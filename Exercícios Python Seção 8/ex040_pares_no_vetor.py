'''Uma função que irá retornar quantos valores pares possui em um array/vetor'''

def pares_vetor(vet):
    pares = 0

    for i in range(len(vet)):
        if vet[i] % 2 == 0 and vet[i] != 0:
            pares = pares + 1
    return pares

lista =[]


NUM = int(input("Digite quantos valores serão digitados: "))
for i in range(NUM):
    lista.append(int(input("Digite um valor: ")))


print(pares_vetor(lista))
