'''Operações com itens de um dicionário'''

def lendo_dados(dados):
    #Transformando lista em str e removendo espaço excedentes à direita
    Frase = ''
    for i in range(len(dados)):
        frase_filha = " ".join(dados[i])
        Frase = Frase + frase_filha + ' '
        if i == len(dados)-1:
            Frase = Frase.rstrip()
            Frase = Frase + '.'

    return Frase


def media_idade_cabelo(dados):
    pessoas = 0
    for i in range(len(dados)):
        if 'C' and 'P' in dados[i]:
            pessoas = pessoas + 1
    return  f'{(pessoas / len(dados)*100):.2f}%'



def maior_idade(dados):
    idades = []
    for i in range(len(dados)):
        for j in range(4):
            if j == 3:
                idades.append(int(dados[i][j]))

    return f'A pessoa mais velha possui {max(idades, key=int)} anos.'


def feminino_maior_idade(dados):
    quantidade = 0
    for i in range(len(dados)):
        for j in range(4):
            if j == 3:
                dados[i][j] = int(dados[i][j])
            if 'F' in dados[i]:
                if j == 3:
                    if dados[i][j] >= 18 and dados[i][j] <=35:
                        if 'A' in dados[i]:
                            if 'L' in dados[i]:
                                quantidade = quantidade + 1
    if quantidade == 1:
        return f'há apenas {quantidade} mulher maior de idade que é loira, possui olhos azuis,e possui menos de 35 anos.'
    return f'possuem {quantidade} mulheres maiores de idade que são loiras, possuem olhos azuis, e são menores de 35 anos.'


dados = []

N = int(input('Quantas pessoas serão digitadas? '))

for i in range(N):
    itens = str(input('Digite o seu Sexo (F = Feminino, M = Masculino), Cor dos olhos (A = azuis, C = castanhos), Cor do cabelo (L = loiro, P = preto, C = castanho) e idade: '))
    dados.append(itens.split())

print()
print(lendo_dados(dados))
print()
print(media_idade_cabelo(dados))
print()
print(maior_idade(dados))
print()
print(feminino_maior_idade(dados))
