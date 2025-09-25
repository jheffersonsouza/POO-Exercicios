from math import sqrt


# Validação de existência de um triangulo com base em pontos de um plano (x,y) e classificação do tipo:
# equilatero, isoceles, escaleno

# Aceitar n pontos, (entre 3 a 4), se for 3 verificar existencia e tipo. Se for 4 verificar se é quadrado ou
# retangulo.

class Ponto:
    def __init__(self, index):
        print("-" * 30)
        print(index, "º Ponto")
        self.x = float(input("Digite a coordenada X: "))
        self.y = float(input("Digite a coordenada Y: "))


def _calcular_distancia(Ponto1, Ponto2):
    return int(sqrt((Ponto2.x - Ponto1.x) ** 2 + (Ponto2.y - Ponto1.y) ** 2))


def verificar_triangulo(A, B, C):
    print('Verificando se existe triângulo com os 3 pontos e caso exista qual seu tipo...')
    segmento_1 = _calcular_distancia(A, B)
    segmento_2 = _calcular_distancia(A, C)
    segmento_3 = _calcular_distancia(B, C)

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


def verificar_quadrilatero(A, B, C, D):
    print('Verificando se existe quadrado com os 4 pontos e caso exista qual seu tipo...')
    pontos = [A, B, C, D]
    distancias = []
    for a in range(0, 4):
        for b in range(a + 1, 4):
            distancias.append(_calcular_distancia(pontos[a], pontos[b]))

    distancias = sorted(distancias)
    for distancia in distancias:
        if distancia == 0:
            print('Pelo menos dois pontos se coincidem, não há como formar uma quadrado ou retângulo.')
            return
    # Últimos elementos sempre são as diagonais
    if distancias[4] == distancias[5]:
        # 4 segmentos iguais
        if distancias[0] == distancias[1] == distancias[2] == distancias[3]:
            print('Os pontos formam um quadrado.')
            return
        # Dois pares de segmentos iguais
        elif distancias[0] == distancias[1] and distancias[2] == distancias[3]:
            print('Os pontos formam um retângulo.')
            return
    print('Os pontos não formam um quadrado ou retângulo.')
    return


pontos = []
for i in range(0, 4):
    pontos.append(Ponto(i + 1))
    if i == 2:
        opt = input('Você deseja continuar? (S/N)').strip().lower()
        if opt == 'n':
            break

if len(pontos) == 3:
    A, B, C = pontos
    verificar_triangulo(A, B, C)
elif len(pontos) == 4:
    A, B, C, D = pontos
    verificar_quadrilatero(A, B, C, D)
else:
    print('Quantia de pontos inválidos, para funcionar é necessário 3 ou 4 pontos.')
