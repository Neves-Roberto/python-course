def dimensoes(matriz):
	linhas = len(matriz)
	for i in matriz:
		colunas = len(i)
	
	dim = str(linhas) + 'X' + str(colunas)
	return dim

m = [[1,2,3],[4,5,6],[7,8,9]]
print('dimensoes da matriz: ', dimensoes(m))
