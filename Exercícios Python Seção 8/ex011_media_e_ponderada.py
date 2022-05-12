'''Calculando media aritmética ou ponderada de notas dos alunos.'''

def media(alternativa, nota1, nota2, nota3):
    '''"if"checando se a média a ser calculada é aritmetica ou ponderada'''
    if alternativa == 'A':
        return (nota1 + nota2 + nota3) / 3
    if alternativa == 'P':
        return (5*nota1 + 3*nota2 + 2*nota3) / 10

alternativa = str(input('Digite "A" para calcular a média aritmética ou "P" para calcular a média ponderada: '))
nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))
nota3 = float(input('Digite o valor da terceira nota:'))

print(f'A média do aluno é: {media(alternativa, nota1, nota2, nota3)}')
