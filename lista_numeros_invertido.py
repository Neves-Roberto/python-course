lista_numeros = []
cont = 1
while cont != 0:
    lista_numeros.append(int(input('Digite um numero inteiro: ')))
    if lista_numeros[-1] == 0:
        cont = 0
tamanho = len(lista_numeros)
lista_numeros_invertida = []
while cont < tamanho:
    lista_numeros_invertida.append(lista_numeros[(tamanho - 1) - cont])
    cont += 1
print(lista_numeros_invertida)
