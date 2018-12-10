# Objetivo: coleta de temperatura e cidada via api do clima tempo
#
# version:1.3
# --------------------------------
from math import ceil
# from tkinter import *
import json
import requests
import time
from xlwt import Workbook
import xlrd
from xlutils.copy import copy
# --------------------------------

token0 = '1f463bfbf867d593ece336c22636eb9e'
token1 = '812ccc8c0b88c1feb866ca74b55b2116'
token2 = '1136491898bd00d3ef40c103414152c0'
# --------------------------------
#diretorio_json = "Z:\json\"
#diretorio_planilha = "Z:\clima_tempo_python\"
#caminho_icones = "i:\\clima_tempo\\realistic\\200px\\"
# --------------------------------
# modo de simulacao gerando arquivos locais
diretorio_json = ""
diretorio_planilha = ""
caminho_icones = ""

# --------------------------------
lista_ids_cidades = [3675, 3589, 3697, 3823, 3771, 3484, 4047, 4234, 4374, 3608, 3837, 3767, 3880, 3960, 4451, 4272,
                     4460, 4274, 3492, 4078, 3852, 3754, 4301, 4364, 3829, 3619, 3824, 4365, 3814]
dicionario_ids_cidades = {3675: "Santos", 3589: "Praia Grande", 3697: "Mongaguá", 3823: "Itanhaém", 3771: "Peruíbe",
                          3484: "São Vicente", 4047: "Cubatão", 4234: "Guarujá", 4374: "Bertioga", 3608: "Registro",
                          3837: "Itariri", 3767: "Pedro de Toledo", 3880: "Juquiá", 3960: "Miracatu", 4451: "Cajati",
                          4272: "Iguape", 4460: "Cananéia", 4274: "Ilha Comprida", 3492: "Sete Barras",
                          4078: "Eldorado", 3852: "Jacupiranga", 3754: "Pariquera-Açu", 4301: "Apiaí",
                          4364: "Barra do Chapéu", 3829: "Itapirapuã Paulista", 3619: "Ribeira", 3824: "Itaóca",
                          4365: "Barra do Turvo", 3814: "Iporanga"}
dicionario_traduz_icones = {'1': 'S', '1n': 'L', '2': 'SN', '2n': 'LN', '2r': 'SN', '2rN': 'LN', '3': 'NC', '3n': 'NC',
                            '3TM': 'N', '4': 'SNC', '4n': 'LNC', '4r': 'SNC', '4rN': 'LNC', '4t': 'SNCR', '4tn': 'LNCR',
                            '5': 'NC', '5n': 'NC', '6': 'NCR', '6n': 'NCR', '7': 'NC', '7n': 'NC', '8': 'NC',
                            '8n': 'NC', '9': 'SN', '9n': 'LN'}
# --------------------------------

def req_clima_tempo(ids, token):
    r = requests.get(
        'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{0}/current?token={1}'.format(ids, token))
    if (r.status_code == 200):
        # conexao ok, retorna json da cidade consultada
        return r.text
    else:
        return "erro"



def extrai_campos_importantes(json_id):
    # retorna lista contendo o que é importante
    if (json_id != "erro"):
        teste = json.loads(json_id)
        arquivo_json = open(diretorio_json + '{0}.json'.format(teste['name']), 'w')
        arquivo_json.write(json_id)
        arquivo_json.close()
        return (teste['name'], ceil(teste['data']['temperature']), teste['data']['icon'])
    else:
        return "erro"


def extrai_campos_importantes_arquivo(json_id):
    # retorna lista contendo o que é importante
    cidade_json = diretorio_json + '{0}.json'.format(dicionario_ids_cidades[json_id])
    arquivo_json = open(cidade_json, 'rt')
    teste = json.loads(arquivo_json.readlines()[0])
    arquivo_json.close()
    return (teste['name'], ceil(teste['data']['temperature']), teste['data']['icon'])


def atualizar_clima_tempo(lista_ids_cidades=lista_ids_cidades):
    pass


def construir_planilha():
    # Construtor de planilha
    workbook_build = Workbook()
    sheet1 = workbook_build.add_sheet('clima_tempo')
    # -----------------------------------
    sheet1.write(0, 0, 'CIDADES')
    sheet1.write(0, 1, 'TEMPERATURA')
    sheet1.write(0, 2, 'ICONE')
    sheet1.write(0, 3, 'NOVO')
    # -----------------------------------
    # TODO: DESABILITAR PROTECAO DO ARQUIVO, OU ATIVAR COMPARTILHAMENTO
    # -----------------------------------
    workbook_build.save(diretorio_planilha + 'clima_tempo_python.xls')


def main(lista_ids_cidades=lista_ids_cidades):
    # função principal
    # path

    extensao = ".png"
    graus = "º"
    print("Versão 1.3")
    time.sleep(5)
    # TODO: VERIFICAR SE A PLANILHA EXISTE, CASO CONTRARIO CRIAR PLANILHA COM A FUNÇÃO construir_planilha()
    construir_planilha()

    read_planilha = xlrd.open_workbook(diretorio_planilha + 'clima_tempo_python.xls')
    workbook_edit = copy(read_planilha)
    w_sheet = workbook_edit.get_sheet(0)
    dicionario_converte_copia = {0: 0, 1: 29, 2: 58, 3: 87, 4: 116}

    for copia in range(5):

        json_clima_tempo = "erro"
        for i in lista_ids_cidades[0:10]:

            json_clima_tempo = req_clima_tempo(i, token2)
            if (json_clima_tempo != "erro" or i == 0):
                dados_importantes = extrai_campos_importantes(json_clima_tempo)

            else:
                print("Excedeu o limite do dia")
                dados_importantes = extrai_campos_importantes_arquivo(i)

            print(
                'Cidade {0} Temperatura: {1} Icone: {2}'.format(dados_importantes[0], str(dados_importantes[1]) + graus,
                                                                caminho_icones + dados_importantes[2] + extensao))
            # GRAVANDO CONTEUDO NA PLANILHA
            # indice representa a linha da planilha
            indice = lista_ids_cidades.index(i) + 2 + dicionario_converte_copia[copia]

            print(indice)
            w_sheet.write(indice - 1, 0, dados_importantes[0])
            w_sheet.write(indice - 1, 1, str(dados_importantes[1]) + graus)
            w_sheet.write(indice - 1, 2, caminho_icones + dados_importantes[2] + extensao)
            w_sheet.write(indice - 1, 3, dicionario_traduz_icones[dados_importantes[2]] + extensao)

        for i in lista_ids_cidades[10:20]:
            json_clima_tempo = req_clima_tempo(i, token1)
            if (json_clima_tempo != "erro" or i == 0):
                dados_importantes = extrai_campos_importantes(json_clima_tempo)

            else:
                print("Excedeu o limite do dia")
                dados_importantes = extrai_campos_importantes_arquivo(i)

            print(
                'Cidade {0} Temperatura: {1} Icone: {2}'.format(dados_importantes[0], str(dados_importantes[1]) + graus,
                                                                caminho_icones + dados_importantes[2] + extensao))
            # GRAVANDO CONTEUDO NA PLANILHA
            indice = lista_ids_cidades.index(i) + 2 + dicionario_converte_copia[copia]
            print(indice)
            w_sheet.write(indice - 1, 0, dados_importantes[0])
            w_sheet.write(indice - 1, 1, str(dados_importantes[1]) + graus)
            w_sheet.write(indice - 1, 2, caminho_icones + dados_importantes[2] + extensao)
            w_sheet.write(indice - 1, 3, dicionario_traduz_icones[dados_importantes[2]] + extensao)

        for i in lista_ids_cidades[20:]:
            json_clima_tempo = req_clima_tempo(i, token0)
            if (json_clima_tempo != "erro" or i == 0):
                dados_importantes = extrai_campos_importantes(json_clima_tempo)

            else:
                print("Excedeu o limite do dia")
                dados_importantes = extrai_campos_importantes_arquivo(i)

            print(
                'Cidade {0} Temperatura: {1} Icone: {2}'.format(dados_importantes[0], str(dados_importantes[1]) + graus,
                                                                caminho_icones + dados_importantes[2] + extensao))
            # GRAVANDO CONTEUDO NA PLANILHA
            indice = lista_ids_cidades.index(i) + 2 + dicionario_converte_copia[copia]
            print(indice)
            w_sheet.write(indice - 1, 0, dados_importantes[0])
            w_sheet.write(indice - 1, 1, str(dados_importantes[1]) + graus)
            w_sheet.write(indice - 1, 2, caminho_icones + dados_importantes[2] + extensao)
            w_sheet.write(indice - 1, 3, dicionario_traduz_icones[dados_importantes[2]] + extensao)

    print("Atualizando Planilha")
    workbook_edit.save(diretorio_planilha + 'clima_tempo_python.xls')
    time.sleep(5)


#main()
# TODO:
# TODO:
