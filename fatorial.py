'''
Exercício 1

Escreva um programa que receba um número natural n na entrada e
imprima n! (fatorial) na saída.

Exemplo:
Digite o valor de n: 5
120
'''
numero = int(input('Digite o valor de n: '))
if numero != 0:
    fatorial = numero
    while numero != 1:
        fatorial = fatorial * (numero -1)
        numero = numero -1
else:
    fatorial = 1
print(fatorial)