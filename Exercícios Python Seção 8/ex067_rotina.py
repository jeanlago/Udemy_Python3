'''Função que recebe como parametro um vetor de caracteres e seu tamanho'''

def getchar(tamanho):
    vet = []
    for i in range(tamanho):
        valor = input('Digite algo: ')
        if valor != '':
            vet.append(list(valor))
        else:
            return vet
    return vet



tamanho=int(input('Digite o tamanho máximo do vetor: '))
print(getchar(tamanho))
