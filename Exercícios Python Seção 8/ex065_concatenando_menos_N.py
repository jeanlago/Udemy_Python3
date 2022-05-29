'''Função que concatena até N letras, e termina com NULL'''

def concatena(palavra1, palavra2, N):
    frase = ''

    for i in range(N):
        frase = frase + palavra2[i]
    return frase + ' ' + palavra1 + ' ' + 'NULL'


palavra1 = str(input('Digite uma palavra: '))
palavra2 = str(input('Digite uma palavra: '))
n = int(input('Digite um número: '))
while n > len(palavra2):
    n = int(input(f'Erro! Digite um valor menor que a quantidade de letras({len(palavra2)}): '))
print(concatena(palavra1,palavra2, n))
