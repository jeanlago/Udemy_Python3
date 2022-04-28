'''Vendo o menor e maior aluno de uma classe'''

NOME = []
ALTURA = []
for i in range(10):
    nome = str(input('Digite o nome do aluno: '))
    altura = float(input('Digite a altura do aluno: '))
    NOME.append(nome)
    ALTURA.append(altura)

alt = 0
for i in range(10):
    if alt < ALTURA[i]:
        alt = ALTURA[i]

pos = ALTURA.index(alt)

print(f'O maior aluno da classe mede {alt} e, se chama: {NOME[pos]}')
