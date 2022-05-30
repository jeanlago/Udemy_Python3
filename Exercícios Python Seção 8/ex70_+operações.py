'''Um racional é qualquer numero da forma p/q sendo p inteiro e 1 inteiro nao nulo.'''

#questão A
def reduz():
    a = int(input('Digite um valor: '))
    b = int(input('Digite outro valor: '))
    return f'{a}/{b}'

def neg(x,y=1):
    return f'{x*-1}/{y}'

def soma(x,y):
    return f'{x+y}/{y}'

def mult(x,y):
    return f'{x*y}/{y}'

def div(x,y):
    return x/y

x = int(input('Digite um valor: '))
y = int(input('Digite um valor: '))

print(reduz())
print()
print(neg(x,y))
print()
print(soma(x,y))
print()
print(mult(x,y))
print()
print(div(x,y))
