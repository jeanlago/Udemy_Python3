'''função recebe temperatura em celsius e devolve em farenheit'''

def temperatura(celsius):
    '''recebendo em celsius e transformando em farenheit'''
    Farenheit = celsius *(9/5) + 32
    return Farenheit


x = float(input('Digite a temperatura em graus Celsius: '))

print(f'A temperatura {x}°C convertida para °F equivale à: {temperatura(x):.2f}°F.')
