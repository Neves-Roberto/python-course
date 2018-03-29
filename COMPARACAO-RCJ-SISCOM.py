import re # biblioteca de expressoes regulares

# baseado na lista de codigos de material
def remove_repetidos(lista):
    tamanho = len(lista)
    lista = sorted(lista)
    if tamanho <= 2:
        return lista
    else:
        posicao1 = 0
        posicao2 = 1
        valor_posicao1 = lista[posicao1]
        valor_posicao_2 = lista[posicao2]
        limite_p1 = tamanho - 2
        limite_p2 = tamanho - 1
        while posicao1 != limite_p1 and posicao2 != limite_p2:
            
            if valor_posicao1 == valor_posicao_2:
                del(lista[posicao2])
                tamanho = len(lista)
                limite_p1 = tamanho - 2
                limite_p2 = tamanho - 1
                valor_posicao_2 = lista[posicao2]
            else:
                posicao1 += 1
                posicao2 = posicao1 + 1
                valor_posicao1 = lista[posicao1]
                valor_posicao_2 = lista[posicao2]
                
        if valor_posicao1 == valor_posicao_2:
            del (lista[posicao2])
    return lista

def busca_codigo_material(lista_rcj,lista_codigo_material):# lista_codigo_material deve estar com elementos unicos, sem repetidos
    '''Baseado na lista de material gera lista com os titulos pesquisando na
na lista do rcj'''
    lista_de_materiais = []
    for itens_codigo_material in lista_codigo_material:
        for itens_lista_rcj in lista_rcj:
            if itens_lista_rcj.find(itens_codigo_material) == 0:
                lista_de_materiais.append(itens_lista_rcj)
                break
    return lista_de_materiais
    


def cria_lista(arquivo):
    ''' recebe um arquivo aberto e devolve uma lista'''
    lista_de_material = []
    arq = arquivo.readlines() # leitura linha a linha do arquivo
    for linha_arq in arq:
        linha_arq = linha_arq.rstrip() # retira as linhas em branco
        lista_de_material.append(linha_arq)
    return lista_de_material

def extrai_codigo_material(lista):
    ''' recebe lista e retorna os codigos de material para uma lista'''
    codigos_de_material = []
    er1 = re.compile(r'^\d{6}') # verifica um padrao de 6 digitos referente ao codigo de material
    for i in lista:
        codigos_de_material.append(er1.match(i).group())
    return codigos_de_material # retorna lista com os codigos d material                  

def main():
        
    # Abrindo arquivos com as listas    
    arquivo1 = open('LISTA_RCJ.TXT','r')
    arquivo2 = open('LISTA_SISCOM.TXT','r')
    arquivo_out = open('COMPARACAO-RCJ-SISCOM.txt','w')

    # Criando lista para manipulacao
    lista_do_arquivo_1 = cria_lista(arquivo1)
    lista_do_arquivo_2 = cria_lista(arquivo2)
    
    
    # Criando listas somente com o codigo de material, pois este eh unico
    codigos_arquivo_1 = extrai_codigo_material(lista_do_arquivo_1)
    codigos_arquivo_2 = extrai_codigo_material(lista_do_arquivo_2)


    codigos_arquivo_1_sem_repetidos = remove_repetidos(codigos_arquivo_1)
    codigos_arquivo_2_sem_repetidos = remove_repetidos(codigos_arquivo_2)

    codigos_arquivo_1 = codigos_arquivo_1_sem_repetidos[:]
    codigos_arquivo_2 = codigos_arquivo_2_sem_repetidos[:]#atualizando os codigos

    lista_do_arquivo_1_sem_repetidos = busca_codigo_material(lista_do_arquivo_1,codigos_arquivo_1)
    lista_do_arquivo_2_sem_repetidos = busca_codigo_material(lista_do_arquivo_2,codigos_arquivo_2)

    lista_do_arquivo_1 = lista_do_arquivo_1_sem_repetidos[:]
    lista_do_arquivo_2 = lista_do_arquivo_2_sem_repetidos[:]#atualizando os codigos

    
    # Varrendo as duas listas e limpando as repeticoes
    for i in codigos_arquivo_2:
        for j in codigos_arquivo_1:
            if j == i:
                lista_do_arquivo_1.pop(codigos_arquivo_1.index(j))#deleta item da lista normal
                codigos_arquivo_1.pop(codigos_arquivo_1.index(j))#deleta item da lista de codigos
                print(j) # imprime somente os iguais
                break

    
    # Gerando arquivo de saida
    for item_lista_do_arquivo_1 in lista_do_arquivo_1:
        item_lista_do_arquivo_1 = item_lista_do_arquivo_1 + '\n'
        arquivo_out.write(item_lista_do_arquivo_1) #adiciona linhas ao arquivo de saida

    # Fechando os arquivos
    arquivo1.close()
    arquivo2.close()
    arquivo_out.close()

main()#chamada de funcao principal
