'''ex053_terreno'''

TERRENO = float(input("Digite o comprimento do terreno: "))
LARGURA = float(input("Digite a largura do terreno: "))
PRICE = float(input("Digite o valor do metro de tela: "))
AREA = TERRENO * LARGURA
PRICE = AREA * PRICE
print(f"O custo para cercar este terreno com tela é: R${PRICE}")
