def imprime_matriz(matriz):
    for linha in matriz:
        for coluna in linha:
            print(coluna, end="")
            if coluna != linha[-1]:#compara a coluna atual com o ultimo elemento da lista
                print(' ', end='')
        print()
    

'''
def main():
    #minha_matriz = [[1], [2], [3]]
    minha_matriz = [[1, 2, 3], [4, 5, 6]]
    imprime_matriz(minha_matriz)


main()
'''
