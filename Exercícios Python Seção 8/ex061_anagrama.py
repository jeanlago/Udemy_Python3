'''função que verifica se uma palabra é anagrama de outra'''

def anagrama(palavra1, palavra2):
    import unidecode  #remover acento das palavras (esse módulo externo precisa ser instalado)

    palavra1 =  unidecode.unidecode(palavra1)
    palavra2 =  unidecode.unidecode(palavra2)

    contador = 0
    for letra in palavra1:
        if letra in palavra2:
            contador = contador + 1
    if contador == len(palavra1):
        return 'Verdadeiro'
    else:
        return 'Falso'


palavra = str(input('Digite uma palavra: '))
palavra2 = str(input('Digite outra palavra: '))

print(anagrama(palavra.lower(), palavra2.lower()))
