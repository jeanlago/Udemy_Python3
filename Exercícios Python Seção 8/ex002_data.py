'''Recebendo a data/mes/ano e escrevendo por extenso'''

def data(mes):
    '''Esta função recebe o mes como int e retorna por extenso.'''
    if mes == '01':
        mes = 'Janeiro'
    elif mes == '02':
        mes = 'Fevereiro'
    elif mes == '03':
        mes = 'Março'
    elif mes == '04':
        mes = 'Abril'
    elif mes == '05':
        mes = 'Maio'
    elif mes == '06':
        mes = 'Junho'
    elif mes == '07':
        mes = 'Julho'
    elif mes == '08':
        mes = 'Agosto'
    elif mes == '09':
        mes = 'Setembro'
    elif mes == '10':
        mes = 'Outubro'
    elif mes == '11':
        mes = 'Novembro'
    elif mes == '12':
        mes = 'Dezembro'
    return mes


X = str(input('Digite a data: '))
lista = X.split('/')

print(f'{lista[0]} de {data(lista[1])} de {lista[2]}')
