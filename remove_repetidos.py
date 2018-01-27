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
    ponteiro_1 = 0
    ponteiro_2 = 1
    valor_posicao_1 = lista[ponteiro_1]
    valor_posicao_2 = lista[ponteiro_2]
    limite_p1 = len(lista) - 2
    limite_p2 = len(lista) - 1

    while ponteiro_1 != limite_p1:
        if valor_posicao_1 == valor_posicao_2:# and ponteiro_2 != quantidade_lista:
            del (lista[ponteiro_2])
            quantidade_lista = len(lista)#atualiza a quantidade da lista
            limite_p1 = len(lista) - 2
            limite_p2 = len(lista) - 1
            valor_posicao_1 = lista[ponteiro_1]
            valor_posicao_2 = lista[ponteiro_2]
            #if ponteiro_2 != quantidade_lista:
            #    valor_posicao_2 = lista[ponteiro_2]

        else:
            ponteiro_2 += 1
            if ponteiro_2 == quantidade_lista:
                ponteiro_1 += 1
                if ponteiro_1 >= limite_p2:
                    return lista
                else:
                    ponteiro_2 = ponteiro_1 + 1
                    valor_posicao_1 = lista[ponteiro_1]
                    valor_posicao_2 = lista[ponteiro_2]
            else:
                valor_posicao_2 = lista[ponteiro_2]

            #if ponteiro_1 == quantidade_lista:
            #    pass


    #return lista


# return lista

lista = [0, 1, 3, 2, 1, 3, 0, 2]

print(remove_repetidos(lista))
