'''Uma função que retorna a intercalação letra a letra da primeira com a segunda string'''

def intercala(palavra1, palavra2):
    caractere = ''
    for i in range(len(palavra1)):
        if i % 2 == 0:
            caractere = caractere + palavra[i]
        else:
            caractere = caractere + palavra2[i]
    return caractere


palavra = str(input('Digite uma palavra: '))
palavra2 = str(input('Digite outra palavra: '))

print(intercala(palavra, palavra2))
