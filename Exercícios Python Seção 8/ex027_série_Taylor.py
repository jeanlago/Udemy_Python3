'''Função que recebe valor de angulo em graus e calcula o valor do seno desse angulo usando serie de Taylor.'''

def fatorial(n):
    return n * fatorial(n-1) if n > 1 else 1

def taylor_sin(grau):
    pi = 3.141593
    rad = grau * pi / 180
    seno = 0

    for k in range(6):
        seno += (-1) ** k * rad ** (2*k + 1) / fatorial(2*k + 1)

    return seno


ang = float(input('Ângulo (graus): '))

print(round(taylor_sin(ang), 8))
