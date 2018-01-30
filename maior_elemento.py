'''
Exercício 1 - Maior elemento de uma lista

Escreva a função maior_elemento que recebe como parâmetro uma lista com números
inteiros e devolve um número inteiro correspondente ao maior valor presente na lista
recebida.
'''

def maior_elemento(lista):
    lista = sorted(lista)
    return lista[-1]