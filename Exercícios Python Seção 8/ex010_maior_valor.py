'''recebendo 2 numeros e retornando o maior.'''

def comparar(num1, num2):
    '''Checando o maior valor na função.'''
    if num1 > num2:
        return num1
    return num2

num1 = float(input('Digite um valor: '))
num2 = float(input('Digite outro valor:'))

print(f'O maior valor é: {comparar(num1,num2)}')
