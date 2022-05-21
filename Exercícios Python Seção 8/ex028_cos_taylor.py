'''Recebendo o valor de um angulo e calculando o valor do cosseno desse angulo usando serie de Taylor'''


def cos_taylor(x,n):
    import math
    return sum((-1)**k * x**(2*k) / math.factorial(2*k) for k in range(n+1))

num = int(input('Digite o valor em graus: '))
num2 = int(input('Digite o parametro: '))

print(f'O cos deste angulo é: {cos_taylor(num, num2)}')
