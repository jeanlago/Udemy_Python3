'''calculando media, variancia e desvio padrão'''
import numpy

V = []
for i in range(8):
    N = int(input('Digite um número: '))
    V.append(N)

media = numpy.average(V)
variancia = numpy.var(V)
DP = numpy.std(V)

print(media)
print(variancia)
print(DP)
