def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(0)
        matriz.append(linha)

    for i in range(num_colunas):
        for j in range(num_linhas):
            matriz[j][i] = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))

    return matriz
<<<<<<< HEAD
print(cria_matriz(2,3))
=======
print(cria_matriz(2,3))

cria_matriz()
>>>>>>> eb20d2b283e58f13cb9eda878638a49c71a78084
