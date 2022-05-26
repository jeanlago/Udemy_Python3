'''uma função que calcula o desvio padrão.'''


def desvio_padrao(vet,chave='desvio padrão'):
    from math import sqrt

    soma = []
    for i in range(len(vet)):
        soma.append(vet[i]**2)

    M = sum(vet) / len(vet)
    VARIANCIA = sum(soma) / len(vet) - M**2
    DP = sqrt(VARIANCIA)

    chave = chave.title()
    if chave == 'Media' or chave == 'Média':
        return f'{M:.2f}'
    if chave == 'Variancia' or chave == 'Variância':
        return f'{VARIANCIA:.2f}'
    if chave == 'Desvio Padrão' or chave == 'Desvio Padrao':
        return f'{DP:.2f}'

VALORES = []

MODO = str(input('Você deseja saber a média, variância ou desvio padrão? '))
QUANTIDADE = int(input('Quantos números serão digitados: '))
for i in range(QUANTIDADE):
    VALORES.append(int(input('Digite um valor: ')))

print(desvio_padrao(VALORES, MODO))