'''
Exercício 2 - Máximo com 3 parâmetros

Reescreva a função 'maximo' do outro exercício, que devolve o maior valor
dentre dois inteiros recebidos, para que ela passe a receber 3 valores
inteiros como parâmetros e devolva o maior dentre eles.

Note que

maximo(30,14,10) deve devolver 30

maximo(0,-1, 1) deve devolver 1
'''

def maximo(v1, v2, v3):
    if v1 >= v2 and v1 >= v3:
        return v1
    if v2 >= v1 and v2 >= v3:
        return v2
    if v3 >= v1 and v3 >= v2:
        return v3


# etapa de testes

def test_maximo301410():
    assert maximo(30,14,10) == 30


def test_maximo011():
    assert maximo(0, -1, 1) == 1