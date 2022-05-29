'''Função que recebe 2 str e concatena a string'''

def concatene(palavra1, palavra2):
    return palavra2 + ' ' + palavra1

palavra1 = str(input('Digite uma palavra: '))
palavra2 = str(input('Digite uma palavra: '))

print(concatene(palavra1,palavra2))
