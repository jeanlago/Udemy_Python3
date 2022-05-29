'''Uma função que calcula o tamanho de uma string'''

def void_tamanho(palavra):
    return len(palavra)

palavra= str(input('Digite uma palavra: '))

print(f'Esta palavra possui {void_tamanho(palavra)} caracteres')
