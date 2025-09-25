from math import sqrt

index = 1

def getIndex():
    return index


def addIndex(i):
    global index
    index += i


class Ponto:
    def __init__(self):
        print("-" * 25)
        print(getIndex(), "º Ponto")
        self.x = float(input("Digite a coordenada X: "))
        self.y = float(input("Digite a coordenada Y: "))
        addIndex(1)


def dist(Ponto1, Ponto2):
    return int(sqrt((Ponto2.x - Ponto1.x) ** 2 + (Ponto2.y - Ponto1.y) ** 2))


A = Ponto()
B = Ponto()
C = Ponto()

segmento_1 = dist(A, B)
segmento_2 = dist(A, C)
segmento_3 = dist(B, C)

if ((segmento_1 + segmento_2 > segmento_3 and
     segmento_1 + segmento_3 > segmento_2) and
        segmento_2 + segmento_3 > segmento_1):
    print('O triângulo existe!')
    print('Tipo:', end=' ')
    if segmento_1 == segmento_2 == segmento_3:
        print('Equilatero')
    elif segmento_1 == segmento_2 or segmento_1 == segmento_3 or segmento_2 == segmento_3:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('O triângulo não existe!')
