'''função verificando se um número é positivo ou negativo'''

def verificando(numero):
    if numero >= 1:
        return 1
    elif numero == 0:
        return 0
    return -1

x = int(input('Digite um valor inteiro: '))


print(verificando(x))
