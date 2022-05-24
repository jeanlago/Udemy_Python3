'''Função que recebe uma lista e retorna o maior valor nela.'''

def maior_lista(vet):
    return max(vet, key = int)


lista = []

NUM = int(input("Digite quantos valores serão digitados: "))
for i in range(NUM):
    lista.append(int(input("Digite um valor: ")))


print(f'O maior valor na lista é {maior_lista(lista)}')
