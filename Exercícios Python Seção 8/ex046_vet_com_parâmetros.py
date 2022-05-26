'''Função que recebe 3 parâmetros'''

def acoes(vet, passo=0, aritmetica='n'):
    '''vet = array recebido
    passo = se o valor for != 0 então printar a lista ao contrário
    aritmetica se for "s" então mostrar a média dentre os valores digitados.'''
    if passo == 0:
        return vet

    elif passo == 0 and aritmetica == 'S':
        print(vet)
        return f'{sum(vet) / len(vet):.2f}'

    elif passo == 1:

        inverso = []
        print(vet)
        for i in vet [::-1]:
            inverso.append(i)

        return(inverso)

    elif passo == 1 and aritmetica == 'S':

        inverso = []
        print(vet)
        for i in vet [::-1]:
            inverso.append(i)

        print(inverso)
        return f'{sum(vet) / len(vet):.2f}'


passo = int(input('Digite 1 se deseja receber a lista inversa, caso não, digite 0: '))
while passo != 1 and passo != 0:
    passo = int(input('Erro! Digite 1 para receber a lista inversa ou digite 0 para não: '))

media = str(input('Digite "S" se deseja receber a média aritmética, caso não, digite "N": '))
media = media.title()

while media != 'S' and media != 'N':
    media = str(input('Erro! Digite "S"  para receber a média aritmética ou "N" para não: '))
    media = media.title()

vet = ([])
for i in range(3):
    vet.append(int(input('Digite um valor: ')))

print(acoes(vet, passo, media))







