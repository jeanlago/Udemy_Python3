
from random import randint


def calculo_maluco_que_entendi(n=0):
    """
    Recebe um inteiro (n) e realiza o cálculo da série: S = 2/4 + 5/5 + 10/6 + ...
    Onde o valor de 'n' será substituido na formula: S = (N² + 1)/(N + 3), retornando o resultado de cada
    valor resultante da formula na lista_valores e será finalizando com a soma dos valores.
    :param n: Receberá um valor inteiro.
    :return: Retornará o resultado do cálculo da série.
    """
    lista_valores = []
    for n in range(1, n+1):
        lista_valores.append(float(f'{((n ** 2 + 1) / (n + 3)):.2f}'))
    return sum(lista_valores)


numero = randint(1, 10)
print(numero)  # Apenas para verificar o valor de 'numero'
print(calculo_maluco_que_entendi(numero))

