# solicitar o tipo do triangulo e gerar os pontos.
import random


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def mostrar(pontos):
    nomes = ['A', 'B', 'C']
    print('-' * 25)
    print('Pontos:')
    for i, p in enumerate(pontos):
        print(f'{nomes[i]} = ({p.x:.2f}, {p.y:.2f})')
    print('-' * 25)

def _gerar_equilatero():
    A = Ponto(1, 1)
    B = Ponto(2.0, 1)
    C = Ponto(1.87, 1.5)
    pontos = [A, B, C]

    k = random.randint(1, 10)
    for ponto in pontos:
        ponto.x = round(ponto.x * k, 2)
        ponto.y = round(ponto.y * k, 2)

    mostrar([A, B, C])


def _gerar_isosceles():
    A = Ponto(random.randint(1, 10), random.randint(1, 10))
    B = Ponto(A.x + 2, A.y)
    C = Ponto(A.x + 1, A.y + 2)
    mostrar([A, B, C])


def _gerar_escaleno():
    A = Ponto(random.randint(1, 10), random.randint(1, 10))
    B = Ponto(A.x + 3, A.y + 1)
    C = Ponto(A.x + 2, A.y + 4)
    mostrar([A, B, C])


while True:
    print("""
Tipos de triângulos:
1. Equilátero
2. Isósceles
3. Escaleno""")

    opt = input('Escolha uma opção: ')
    if opt == '1':
        _gerar_equilatero()
    elif opt == '2':
        _gerar_isosceles()
    elif opt == '3':
        _gerar_escaleno()
    else:
        print('Opção inválida.')
        continue
    print()
