def dimensoes(matriz):
    dimensao = []
    linhas = len(matriz)
    for i in matriz:
        colunas = len(i)
    
    dim = str(linhas) + 'X' + str(colunas)
    dimensao.append(dim)
    dimensao.append(linhas)
    dimensao.append(colunas)
    return dimensao

def soma_matrizes(m1,m2):
    dim = dimensoes(m1)
    matriz1 = dim[0]
    matriz2 = dim[0]
    linhas = dim[1]
    colunas = dim[2]
    m3 = []
    if matriz1 == matriz2:
        for linha in range(linhas):
            for coluna in range(colunas):
                m3[linha][colunas] = m1[linha][coluna] + m2[linha][coluna]
                print('linha [{}], coluna [{}] = {} '.format(linha,coluna,linha+coluna))
        return 'soma_matrizes(m1, m2) => ' + m3
    else:
        return False

m1 = [[1, 2, 3],[4, 5, 6]]
m2 = [[2, 3, 4],[5, 6, 7]]

soma_matrizes(m1,m2)

def test_soma_matrizes1():
    assert soma_matrizes([[1, 2, 3], [4, 5, 6]], [[2, 3, 4], [5, 6, 7]]) == 'soma_matrizes(m1, m2) => '[[3, 5, 7], [9, 11, 13]]
    
def test_soma_matrizes2():
    assert soma_matrizes([[2, 3], [4, 5, 6]], [[2, 3, 4], [5, 6, 7]]) == 'soma_matrizes(m1, m2) => False'
