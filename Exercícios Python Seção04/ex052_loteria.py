'''ex052_loteria'''

import math
PREMIO = float(input("Digite o valor do prêmio: "))

NOME: [str] = [0 for x in range(3)]
INVEST: [float] = [0 for x in range(3)]

for i in range (3):
    NOME[i] = input(f"qual o nome do {i+1}º usuário? ")
    INVEST[i] = float(input(f"Quanto foi investido pelo {i+1}º usuário? "))
    print()

for i in range(3):
    CALCULO = ((100 * INVEST[i])/PREMIO)
    VALOR_TOTAL = ((PREMIO * CALCULO)/ 100)
    print(f"O usuário {NOME[i]}, irá receber {CALCULO:.2f}%, que corresponde à R${VALOR_TOTAL:.2f} do valor total do prêmio.")
