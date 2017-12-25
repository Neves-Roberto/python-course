#crie um programa que leia um numero real qualquer pelo teclado e mostre a sua porção inteira
#ex digite um numero 6.127 parte real 6
import math
numreal = float(input('Digite um numero real: '))
print('numero digitado {} parte real {} tipo primitivo {}'.format(numreal,math.trunc(numreal),type(numreal)))