#2, 3, 5, 7, 11 ...

'''
algoritimo generico para descobrir numeros primos
ler um numero inteiro positivo

Exercício 1

Escreva um programa que receba um número inteiro positivo na entrada e
verifique se é primo. Se o número for primo, imprima "primo".
Caso contrário, imprima "não primo".

Exemplos:

Digite um número inteiro: 11

primo

Digite um número inteiro: 12

não primo
'''
primalidade = True

numero = int(input('Digite um número inteiro: '))
i = 2
if numero == 1 or numero == 2 or numero == 3:
    primalidade = True
else:
    while i != numero and primalidade:
        if numero % i == 0:
            primalidade = False
        else:
            primalidade = True
        i = i + 1
    

if primalidade:
    print('primo')
else:
    print('não primo')