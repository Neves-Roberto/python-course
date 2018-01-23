'''
Exercício 1 - Primos

Escreva a função n_primos que recebe um número inteiro maior ou igual a 2
como parâmetro e devolve a quantidade de números primos que existem entre 2
e n (incluindo 2 e, se for o caso, n).
'''

def n_primos(n):
    soma_primos = 0
    cont = 2
    while cont <= n:
        if é_primo(cont):
            soma_primos += 1
        cont += 1
    return soma_primos

def é_primo(n):
    #TODO implementar verificação de erro quando digitado 1, zero ou negativo
    i = 2
    primalidade = True
    while i != n and primalidade:
        if n % i == 0:
            primalidade = False
        i = i + 1
    return primalidade
    
def main():
    n = int(input('Digite um interiro maior que 2: '))
    print(n_primos(n))
    

main()