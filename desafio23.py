#faça um programa leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
#ex: digite um numero:1834
#unidade:4
#dezena:3
#centena:8
#milhar:1
#tentar fazer com string e com numeros

#modo com string
#numero = '1234'
'''
numero = str(input('Digite um numero de 0 ate 9999: '))
print('unidade: {}'.format(numero[3]))
print('dezena: {}'.format(numero[2]))
print('centena: {}'.format(numero[1]))
print('milhar: {}'.format(numero[0]))
'''
import math
#modo com numero
#numero = 12
numero = int(input('Digite um numero de 0 ate 9999: '))
print('unidade: {}'.format(math.trunc(numero/1)%10))
print('dezena: {}'.format(math.trunc(numero/10)%10))
print('centena: {}'.format(math.trunc(numero/100)%10))
print('milhar: {}'.format(math.trunc(numero/1000)%10))
