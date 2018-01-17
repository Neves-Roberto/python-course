'''
Exercício 1

Escreva um programa que receba um número natural n na entrada e
imprima n! (fatorial) na saída.

Exemplo:
Digite o valor de n: 5
120
'''
def fatorial(k):
    '''(int) -> int

    Recebe um inteiro k e retorna o valor de k!

    Pre-condicao: supoe que k eh um numero inteiro nao negativo.
    '''

    k_fat = 1
    cont = 1
    while cont < k:
        cont += 1       # o mesmo que cont = cont + 1
        k_fat *= cont   # o mesmo que k_fat = k_fat * cont

    return k_fat


#numero = int(input('Digite o valor de n: '))

#print(fatorial(numero))

def test_fatorial0():
    assert fatorial(0) == 1

def test_fatorial1():
    assert fatorial(1) == 1
    
def test_fatorial2():
    assert fatorial(2) == 2
    
def test_fatorial5():
    assert fatorial(5) == 120