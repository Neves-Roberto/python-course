'''
Exercício 2 - Invertendo sequência

Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma
sequência de números inteiros terminados por 0 e imprima todos os valores em ordem
inversa. Note que 0 (ZERO) não deve fazer parte da sequência.

Exemplo:
Digite um número: 1
Digite um número: 7
Digite um número: 4
Digite um número: 0

4
7
1

'''

lista_numeros = []
cont = 1
while cont != 0:
    lista_numeros.append(int(input('Digite um numero inteiro: ')))
    if lista_numeros[-1] == 0:
        cont = 0
tamanho = len(lista_numeros) - 2

for lista_invertida in range(tamanho,-1,-1):
    print(lista_numeros[lista_invertida])
'''
for i in range(10, -1, -1):
    print(i)
'''