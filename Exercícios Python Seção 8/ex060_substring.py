'''Retornando o primeiro elemento de uma substring dentro de uma string'''

def elemento_na_linha(linha):
    palavra = linha

    if type(palavra) == str:
        return palavra[:1]
    else:
        return -1







linha = input('Digite algo: ')

print(elemento_na_linha(linha))



