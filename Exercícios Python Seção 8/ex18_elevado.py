'''Recebendo 2 parâmetros e retornando elevado.'''

def exponenciacao(X, Y):
    soma = X
    for i in range(Y-1):
        soma = soma * X
    return soma
    #ou return X ** Y

x = int(input('Digite um valor para o x: '))
y = int(input('Digite um valor para o y: '))

print(exponenciacao(x,y))
