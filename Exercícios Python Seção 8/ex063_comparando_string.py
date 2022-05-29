'''Comparando se uma string é igual à outra'''

def compare(palavra1,palavra2):
    if palavra1 == palavra2:
        return 'São iguais'
    else:
        return 'Não são iguais'

palavra1 = str(input('Digite uma palavra: '))
palavra2 = str(input('Digite uma palavra: '))

print(compare(palavra1.lower(), palavra2.lower()))
