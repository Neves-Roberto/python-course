def cria_matriz(linhas,colunas,valor):
	matriz = []
	for i in range(linhas):
		linhas = []
		for j in range(colunas):
			linhas.append(valor)
		matriz.append(linhas)
	return matriz

def cria_matriz_bidimensional(matriz_x_y):
	for linhas in matriz_x_y:
		for colunas in linhas:
			print(colunas, end= " ")
		print('')
	
	

def main():
	print(cria_matriz_bidimensional(cria_matriz(10,1,'{-x-}')))

main()


minha_matriz = [[1], [2], [3]]
minha_matriz = [[1, 2, 3], [4, 5, 6]]