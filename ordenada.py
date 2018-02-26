def ordenada(lista):
	'''Recebe uma lista de inteiros e devolve True se a lista estiver ordenada 
	False se a lista não estiver ordenada
	'''
	lista_ordenada = sorted(lista)
	if lista == lista_ordenada:
		return True
	return False
