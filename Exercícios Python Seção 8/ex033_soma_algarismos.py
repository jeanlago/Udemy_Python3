'''Recebendo um valor e retornando a soma dos algarismos. '''

def soma_algarismos(NUM):
    return [int(a) for a in str(NUM)]

valor = int(input("Digite o valor: "))

print(f'A divisão do valor {valor} em algarismos fica:',end=' ')
#O operador * em Python pode ser usado para descompactar objetos.
# Ele descompacta todos os elementos de uma lista e os imprime sem os colchetes, conforme mostrado abaixo.
print(*soma_algarismos(valor), sep=' + ',end=' = ')
print(sum(soma_algarismos(valor)))

