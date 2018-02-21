
def dimensoes(matriz):
	linhas = len(matriz)
	for i in matriz:
		colunas = len(i)
	
	dim = str(linhas) + 'X' + str(colunas)
	print(dim)

#minha_matriz = [[1], [2], [3]]
#var = dimensoes(minha_matriz)
#print(var)

'''

def test_dimensoes_1():
	assert dimensoes([[1, 2], [3, 4]]) == '2X2'

def test_dimensoes_2():
	assert dimensoes(([[1, 1], [1, 1]])) == '2X2'

def test_dimensoes_3():
	assert dimensoes(([[1, 2, 7, 1], [3, 4, 8, 1], [1, 2, 3, 1], [2, 3, 6, 7]])) == '4X4'

def test_dimensoes_4():
	assert dimensoes(([[1, 2, 7, 1], [3, 4, 8, 1], [1, 2, 3, 1]])) == '3X4'

def test_dimensoes_5():
	assert dimensoes(([[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]])) == '4X3'

def test_dimensoes_6():
	assert dimensoes(([[1], [2]])) == '2X1'

def test_dimensoes_7():
	assert dimensoes(([[1, 2]])) == '1X2'

def test_dimensoes_8():
	assert dimensoes(([[1]])) == '1X1'

def test_dimensoes_9():
	assert dimensoes([[1], [2], [3]]) == '3X1'
'''