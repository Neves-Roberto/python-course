import re # biblioteca de expressoes regulares
import glob, os, datetime
import math
from math import trunc

def ler_xls():
    from xlrd import open_workbook

    xls = open_workbook('Envio_SAN_27_03_2018.xls')
    
    for sheets in xls.sheets():
        list1 = []
        for rows in range(sheets.nrows):
            list1.append(str(sheets.cell(rows, 1).value))

    list2 = []
    for item in list1:
        
        if not (item == 'CÓD MAT' or item == ''):
            
            list2.append(trunc(float(item)))

    return list2


def lista_arquivo_filtro_data(lista_de_arquivos,patch,data):
    
    print('lista de arquivos compativeis com a data ', data)
    lista = []
    for item in lista_de_arquivos:
        if extrai_data_arquivo(patch + item) == data:
            lista.append(item)
    return lista


def extrai_data_arquivo(nome_arquivo):
    info_arquivo = os.stat(nome_arquivo)
    return str(datetime.datetime.fromtimestamp(info_arquivo.st_mtime).date())

# gera uma lista com os arquivos de interesse
def listar_arquivos(patch,extensao):
    os.chdir(patch)
    return glob.glob('*.' + extensao)

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
    patch1 = "C:/Users/dkscr/Downloads/compara_rcj_siscom-20180328T214602Z-001/compara_rcj_siscom/rcj/"
    patch2 = "C:/Users/dkscr/Downloads/compara_rcj_siscom-20180328T214602Z-001/compara_rcj_siscom/siscom/"
    extensao = 'mxf'

    # Criando lista para manipulacao
    #lista_do_arquivo_1 = cria_lista(arquivo1)
    #lista_do_arquivo_2 = cria_lista(arquivo2)
    lista_do_arquivo_1 = listar_arquivos(patch1,extensao)
    lista_do_arquivo_2 = listar_arquivos(patch2,extensao)
    print(ler_xls())

    #checar data
    #data = '2018-03-29'
    data = input('Digite a data no formato AAAA-MM-DD : ')
    lista_do_arquivo_1_filtrada = lista_arquivo_filtro_data(lista_do_arquivo_1,patch1,data)
    lista_do_arquivo_1 = lista_do_arquivo_1_filtrada[:]

    
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
    a = input("PRESIONE PARA ENCERRAR!")

main()#chamada de funcao principal
