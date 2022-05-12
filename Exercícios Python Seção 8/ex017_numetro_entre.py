'''Recebendo 2 numeros int positivos e retornando a soma entre os mesmos.'''

def soma_entre(num1, num2):
    soma = 0
    for i in range(num1+1, num2):
        soma = soma + i
    return soma


x = int(input('Digite um valor: '))
y = int(input('Digite outro valor: '))

print(f'A soma dos numeros existentes entre o valor {x} e {y} é: {soma_entre(x, y)}')
