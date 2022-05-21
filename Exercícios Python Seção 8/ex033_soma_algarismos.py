'''Recebendo um valor e retornando a soma dos algarismos. '''

def soma_algarismos(NUM):
    return [int(a) for a in str(NUM)]

valor = int(input("Digite o valor: "))

print(f'A divisão do valor {valor} em algarismos fica:',end=' ')
print(*soma_algarismos(valor), sep=' + ',end=' = ')
print(sum(soma_algarismos(valor)))

