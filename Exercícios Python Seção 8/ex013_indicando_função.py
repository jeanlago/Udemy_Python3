'''Recebendo 2 valores numericos e um simbolo para indicar o que a função deve fazer'''

def calculo(valor1, valor2, símbolo):
    if símbolo == '+':
        return valor1 + valor2
    elif símbolo == '-':
        return valor1 - valor2
    elif símbolo == '/':
        return valor1 / valor2
    elif símbolo == '*':
        return valor1 * valor2

operação = str(input('Digite o símbolo de qual operação será realizada (+, -, /, *): '))
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

print(f'O resultado da operação é: {calculo(valor1,valor2,operação):.2f}')