'''Exercício 1 - Distância entre dois pontos

Receba 4 números inteiros na entrada. Os dois primeiros devem corresponder,
respectivamente, às coordenadas x e y de um ponto em um plano cartesiano.
Os dois últimos devem corresponder, respectivamente, às coordenadas x e y
de um outro ponto no mesmo plano.

Calcule a distância entre os dois pontos. Se a distância for maior ou
igual a 10, imprima

longe

na saída. Caso o contrário, quando a distância for menor que 10, imprima

perto'''
from math import sqrt
p1x = int(input('Digite o valor de X do ponto P1: '))
p1y = int(input('Digite o valor de Y do ponto P1: '))
p2x = int(input('Digite o valor de X do ponto P2: '))
p2y = int(input('Digite o valor de Y do ponto P2: '))

distancia = sqrt(((p2x-p1x) ** 2) + ((p2y-p1y) ** 2))
if (distancia >= 10):
    print('longe ')
else:
    print('perto ')
