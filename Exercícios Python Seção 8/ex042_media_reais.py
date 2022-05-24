'''Vetor que recebe números reais e retorna a média deles.'''

def media_reais(vet):
    '''função para calcular média de números reais'''
    '''round é uma função para arredondar com 2 casas decimais.'''
    return round(sum(vet) / len(vet), 2)

lista = []


NUM = int(input("Digite quantos valores serão digitados: "))
for i in range(NUM):
    lista.append(float(input("Digite um valor real: ")))


print(f'a média dos valores {lista} é {media_reais(lista)}')
