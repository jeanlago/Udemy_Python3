'''manipulando vetor'''

lista = []

for i in range(5):
    X = float(input("Digite um número: "))
    lista.append(X)

for i in range(5):
    X = int(input("Digite o código: "))
    if X == 0:
        print('Obrigado por testar o programa! :)')
        break
    elif X == 1:
        print(lista)
        break
    elif X == 2:
        print(lista[::-1])
        break
    elif X != 1 or X != 2:
        print("O código digitado é invalido.")
        break
