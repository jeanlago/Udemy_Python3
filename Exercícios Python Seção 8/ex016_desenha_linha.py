'''Criando uma função para desenhar uma linha na tela'''

def desenha_linha(tamanho):
   desenho = '='
   return desenho * tamanho

tamanho = int(input("Digite o tamanho da linha: "))

print(desenha_linha(tamanho))
