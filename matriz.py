def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        linha = [] # cria linha
        for j in range(num_colunas):
            linha.append(0)
        #adiciona a linha a matriz
        matriz.append(linha)

    return matriz
