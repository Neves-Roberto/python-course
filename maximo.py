'''
Exercício 1 - Máximo

Escreva a função maximo que recebe 2 números inteiros como parâmetro e
devolve o maior deles.

Note que

maximo(3,4) deve devolver 4

maximo(0,-1) deve devolver 0
'''
def main():
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    print(maximo(valor1, valor2))
    
def maximo(a, b):
    if a >= b:
        return a
    else:
        return b

main()
    
'''
#desenvolvendo os testes padronizados
def test_maximo34():
    assert maximo(3, 4) == 4
    
def test_maximo01():
    assert maximo(0, -1) == 0
'''