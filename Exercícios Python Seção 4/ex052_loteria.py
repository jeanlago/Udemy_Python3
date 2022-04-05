'''ex052_loteria'''

PREMIO = float(input("Digite o valor do prêmio: "))

NOME: [str] = [0 for x in range(3)]
INVEST: [float] = [0 for x in range(3)]
SOMA:[float] = 0

for i in range (3):
    NOME[i] = input(f"qual o nome do {i+1}º usuário? ")
    INVEST[i] = float(input(f"Quanto foi investido pelo {i+1}º usuário? "))
    SOMA = SOMA + INVEST[i]
    print()

for i in range(3):
    CALCULO = ((100 * INVEST[i])/SOMA)
    VALOR_TOTAL = ((CALCULO * PREMIO)/100)
    print(f"O usuário {NOME[i]}, irá receber {CALCULO:.2f}%, que corresponde à R${VALOR_TOTAL:.2f} do valor total do prêmio.")
