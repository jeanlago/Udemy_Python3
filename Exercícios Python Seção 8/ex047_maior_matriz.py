'''Função que retorna a quantidade de valores maiores que 10 em matriz'''

def maior_que_dez(lista):
    maior = 0

    for i in range (len(lista)):
        for j in range(len(lista)+1):
            if lista[i][j] > 10:
                maior = maior + 1
    return maior



lista = []

for i in range(4):
    lista_filha=[]
    for j in range(4):
        lista_filha.append(int(input('Digite um valor: ')))
    lista.append(lista_filha)

print(f'A matriz digitada, possui {maior_que_dez(lista)} números maiores que 10.')