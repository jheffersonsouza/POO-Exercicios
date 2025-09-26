import math
# Validação de existência de um triangulo com base em pontos de um plano (x,y) e classificação do tipo:
# equilatero, isoceles, escaleno

# Aceitar n pontos, (entre 3 a 4), se for 3 verificar existencia e tipo. Se for 4 verificar se é quadrado ou
# retangulo.

class Ponto:
    def __init__(self, index):
        print("-" * 30)
        print(f"{index}º Ponto")
        self.x = float(input("Digite a coordenada X: "))
        self.y = float(input("Digite a coordenada Y: "))


def calcular_distancia(ponto1, ponto2):
    return math.sqrt((ponto2.x - ponto1.x) ** 2 + (ponto2.y - ponto1.y) ** 2)


def verificar_igualdade_com_tolerancia(segmento_A, segmento_B):
    return math.isclose(segmento_A, segmento_B, rel_tol=0.05, )


def verificar_triangulo(A, B, C):
    print('Verificando se existe triângulo com os 3 pontos e caso exista qual seu tipo...')
    segmento_AB = calcular_distancia(A, B)
    segmento_AC = calcular_distancia(A, C)
    segmento_BC = calcular_distancia(B, C)

    if (segmento_AB + segmento_AC > segmento_BC and
            segmento_AB + segmento_BC > segmento_AC and
            segmento_AC + segmento_BC > segmento_AB):
        print('O triângulo existe!')
        print('Tipo:', end=' ')
        if (verificar_igualdade_com_tolerancia(segmento_AB, segmento_AC) and
                verificar_igualdade_com_tolerancia(segmento_AB, segmento_BC)):
            print('Equilátero')
        elif (verificar_igualdade_com_tolerancia(segmento_AB, segmento_AC) or
              verificar_igualdade_com_tolerancia(segmento_AB, segmento_BC) or
              verificar_igualdade_com_tolerancia(segmento_AC, segmento_BC)):
            print('Isósceles')
        else:
            print('Escaleno')
    else:
        print('Os pontos são colineares. O triângulo não existe!')


def verificar_quadrilatero(A, B, C, D):
    print('Verificando se os 4 pontos formam um quadrado ou retângulo...')
    pontos = [A, B, C, D]
    segmentos = []
    for i in range(4):
        for j in range(i + 1, 4):
            distancia_sq = (pontos[j].x - pontos[i].x) ** 2 + (pontos[j].y - pontos[i].y) ** 2
            if distancia_sq == 0:
                print('Pelo menos dois pontos coincidem. Não é possível formar um quadrilátero válido.')
                return
            segmentos.append(distancia_sq)
    segmentos.sort()



    lados = segmentos[:4]
    diagonais = segmentos[4:]

    # Dos 4 segmentos de lados, ha dois pares de segmentos que sao iguais
    lados_iguais = verificar_igualdade_com_tolerancia(lados[0], lados[1]) and verificar_igualdade_com_tolerancia(
        lados[2], lados[3])

    if verificar_igualdade_com_tolerancia(diagonais[0], diagonais[1]) and lados_iguais:
        # Se os 4 segmentos de lados são iguais, é um quadrado.
        if verificar_igualdade_com_tolerancia(lados[0], lados[3]):
            print('Os pontos formam um QUADRADO.')
        else:
            print('Os pontos formam um RETÂNGULO.')

    else:
        print('Os pontos não formam um quadrado ou retângulo.')


pontos = []
max_pontos = 4
for i in range(max_pontos):
    pontos.append(Ponto(i + 1))
    if i == 2:
        opt = input('Você deseja adicionar um 4º ponto? (S/N) ').strip().lower()
        if opt == 'n':
            break

if len(pontos) == 3:
    verificar_triangulo(pontos[0], pontos[1], pontos[2])
elif len(pontos) == 4:
    verificar_quadrilatero(pontos[0], pontos[1], pontos[2], pontos[3])
else:
    print('Número de pontos inválido. São necessários 3 ou 4 pontos.')
