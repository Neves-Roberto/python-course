'''
Exercício 2 - Primos

Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2
como parâmetro e devolve o maior número primo menor ou igual ao número
passado à função

Note que

maior_primo(100) deve devolver 97

maior_primo(7) deve devolver 7

Dica: escreva uma função éPrimo(k) e faça um laço percorrendo os números
até o número dado checando se o número é primo ou não; se for, guarde numa
variável. Ao fim do laço, o valor armazenado na variável é o maior primo
encontrado.

'''
def ePrimo(k):
    pass

def maior_primo(x):
    pass



#etapa de testes

def test_maior_primo100():
    assert maior_primo(100) == 97
    
def test_maior_primo7():
    assert maior_primo(7) == 7