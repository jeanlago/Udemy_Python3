'''Recebendo hora minuto e segundo e transformando em segundo'''

def hora_segundo(hora, minuto, segundo):
    minuto = hora * 60 + minuto
    segundo = minuto * 60 + segundo
    return segundo

x = int(input('Digite a quantidade de horas: '))
y = int(input('Digite a quantidade de minutos: '))
z = int(input('Digite a quantidade de segundos: '))

print(f'A conversão de hora:minuto:segundo em segundos é:{hora_segundo(x,y,z)}')
