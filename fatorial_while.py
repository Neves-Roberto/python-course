#faz o calculo de fatorial em loop das entradas digitadas

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

while True:
    numero = int(input('Digite um numero para calculo do fatorial: '))
    print('O fatorial de {} é {}'.format(numero,fatorial(numero)))