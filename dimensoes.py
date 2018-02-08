def dimensoes(matriz):
	linhas = len(matriz)
	for i in matriz:
		colunas = len(i)
	
	dim = str(linhas) + 'X' + str(colunas)
	return dim
