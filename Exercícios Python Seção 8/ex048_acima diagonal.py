'''função para calcular os valores acima da diagonal principal'''

def acima_função(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)+1):
            if i > 0:
                if i == j:
                    soma = soma + matriz[i-1][j]
    return soma


matriz = []
for i in range(3):
    matriz_filha = []
    for j in range(3):
        matriz_filha.append(int(input('Digite um valor: ')))
    matriz.append(matriz_filha)

print(f'A soma dos elementos acima da diagonal principal é: {acima_função(matriz)}')
