def dimensoes(matriz):
    dimensao = []
    linhas = len(matriz)
    for i in matriz:
        colunas = len(i)
    dimensao.append(linhas)
    dimensao.append(colunas)
    return dimensao

def sao_multiplicaveis(m1, m2):
    col1 = dimensoes(m1)[1]
    lin2 = dimensoes(m2)[0]
    
    if col1 == lin2:
        return True
    else:
        return False

def test_01():
    m1 = [[1]]
    m2 = [[1, 2, 3]]
    assert sao_multiplicaveis(m1, m2) == True


