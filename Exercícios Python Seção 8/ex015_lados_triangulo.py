'''Recebendo 3 valores maiores 0 (lados de um triangulo) e calculando'''

def triangulo(lado1, lado2, lado3):
    if lado1 + lado2 > lado3:
        print('Estes números digitados formam um triângulo!')
        if lado1 == lado2 and lado1 != lado3:
            return 'Este é um triângulo isósceles'
        elif lado1 == lado3 and lado1 != lado2:
            return 'Este é um triângulo isósceles'
        elif lado1 == lado2 and lado1 == lado3:
            return 'Este é um triângulo equilátero'
        else:
            return 'Este é um triângulo escaleno'
    return 'Os números digitados não formam um triângulo!'



lista= []
for i in range(3):
    x = int(input('Digite um valor: '))
    if x <= 0:
        while x <= 0:
            x = int(input('Erro! Por favor, digite um valor maior que 0: '))
    lista.append(x)

lado1, lado2, lado3 = lista

print(triangulo(lado1,lado2,lado3))


