'''Verificando se esse valor está dentro de um retângulo '''


def dentro_ret(v1,v2,p):
    if v1[0] < p[0] < v2[0]:
        if v1[1] < p[1] < v2[1]:
            return '1'
    return '0'


v1 = (7,5)
v2 = (9,7)
p = (8, 6)

print(dentro_ret(v1,v2,p))
