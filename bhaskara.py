'''Exercício 2 - Desafio da videoaula

Como pedido na videoaula desta semana, escreva um programa que calcula as
raízes de uma equação do segundo grau.

O programa deve receber os parâmetros a, b, e c da equação ax2+bx+c,
respectivamente, e imprimir o resultado na saída da seguinte maneira:

Quando não houver raízes reais imprima:

esta equação não possui raízes reais

Quando houver apenas uma raiz real imprima:

a raiz desta equação é X

onde X é o valor da raiz

Quando houver duas raízes reais imprima:

as raízes da equação são X e Y

onde X e Y são os valor das raízes.

Além disso, no caso de existirem 2 raízes reais,
elas devem ser impressas em ordem crescente, ou seja,
X deve ser menor que Y.

Δ < 0, então a equação não possui resultados reais;

Δ = 0, então a equação possui apenas um resultado real ou possui dois resultados iguais (essas duas afirmações são equivalentes);

Δ > 0, então a equação possui dois resultados distintos reais.
'''
from math import sqrt
print('Digite os parâmetros a, b, e c da equação ax2+bx+c')

a = float(input('Ditige o parametro a: '))
b = float(input('Ditige o parametro b: '))
c = float(input('Ditige o parametro c: '))

delta = ((b ** 2) - (4 * a * c))

if (delta < 0):
    print('esta equação não possui raízes reais')
elif (delta > 0):
    # imprimir as raizes de forma crescente
    x1 = ((b * (-1)) + sqrt(delta)) / (2 * a)
    x2 = ((b * (-1)) - sqrt(delta)) / (2 * a)
    if (x1 > x2):
        aux = x1
        x1 = x2
        x2 = aux
    print('as raízes da equação são {} e {}'.format(x1, x2))
else:
    x1 = ((b * (-1)) + sqrt(delta)) / (2 * a)
    print('a raiz desta equação é {}'.format(x1))

