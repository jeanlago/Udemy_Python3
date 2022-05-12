'''calculando o cons=umo em Km/l'''

def consumo(quilometros, litros):
    Kml = quilometros / litros
    if Kml < 8:
        return 'Venda o carro!'
    elif Kml > 7 and Kml < 14:
        return 'Econômico!'
    elif Kml > 12:
        return 'Super econômico!'



quilometros = float(int(input("Digite a quantidade de Km percorrido: ")))
litros = float(input("Digite a quantidade final de litros: "))

print(consumo(quilometros, litros))