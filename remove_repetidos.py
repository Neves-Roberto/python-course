'''
Exercício 1 - Removendo elementos repetidos

Escreva a função remove_repetidos que recebe como parâmetro uma lista 
com números inteiros, verifica se tal lista possui elementos repetidos e os remove. 
A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. 
A lista devolvida deve estar ordenada.

Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?
'''
def remove_repetidos(lista):
	quantidade_lista = len(lista)
	posicao_1 = 0
	posicao_2 = 1
	
	while posicao_1 != quantidade_lista:
		if lista[posicao_1] == lista[posicao_2]:
			del(lista[posicao_2])
			quantidade_lista = len(lista)
		else:
			posicao_2 +=1
	posicao_1 += 1
	
	print(lista)
	print(lista.sort())
	print(sorted(lista))
	#return lista
	
lista = [0, 1, 2, 1, 2, 1]

remove_repetidos(lista)

  