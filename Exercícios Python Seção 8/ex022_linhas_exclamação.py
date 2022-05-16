'''Criando uma função para escrever n linhas de "!"'''

def escreve_exclamação(VALOR):
    for QUANTIDADE in range(1, VALOR):
        CARACTERE = '!'
        print(CARACTERE * QUANTIDADE)
    return CARACTERE * VALOR


VALOR = int(input("Digite qual a quantidade de '!' você deseja: "))

print(escreve_exclamação(VALOR))
