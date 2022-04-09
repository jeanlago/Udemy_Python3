'''Lendo nota de 15 alunos e armazenando-nas em um vetor
em seguida calculando a média.'''

lista = []
media = 0
for i in range(15):
    X = float(input('Digite a nota do aluno: '))
    lista.append(X)

for i in range(15):
    media = media + lista[i]

media = media / 15
print(f'A média geral dos alunos é: {media:.2f}')
