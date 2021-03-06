# Objetivo: coleta de temperatura e cidada via api do clima tempo
#
# version:1.4
# --------------------------------
import LibClimaTempo as clima
import time
import xlrd
from xlutils.copy import copy
import Gerador_html_clima_tempo
# --------------------------------
token0 = 'fe028fd71ec9e3dde761ab29b3d977fd' # token projetos.tvtribuna.com
#token0 = '1f463bfbf867d593ece336c22636eb9e'
#token1 = '812ccc8c0b88c1feb866ca74b55b2116'
#token2 = '1136491898bd00d3ef40c103414152c0'
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
lista_ids_cidades = [3675, 3484, 3589,4234,4047, 3697, 4374, 3823, 4078,3771,3837,3960,3880,3608, 4272,3492, 4274,3754,3852,4451, 4460,3814,4365,4301,3824,4364,3619,3829]
dicionario_ids_cidades = {3675: "Santos", 3484: "São Vicente", 3589: "Praia Grande",4234: "Guarujá", 4047: "Cubatão", 3697: "Mongaguá", 4374: "Bertioga", 3823: "Itanhaém", 4078: "Eldorado",3771: "Peruíbe",3837: "Itariri",3767: "Pedro de Toledo",3960: "Miracatu",3880: "Juquiá",3608: "Registro", 4272: "Iguape",3492: "Sete Barras", 4274: "Ilha Comprida",3754: "Pariquera-Açu",3852: "Jacupiranga",4451: "Cajati", 4460: "Cananéia",3814: "Iporanga",4365: "Barra do Turvo",4301: "Apiaí",3824: "Itaóca",4364: "Barra do Chapéu", 3619: "Ribeira",3829: "Itapirapuã Paulista" }
dicionario_traduz_icones = {'1': 'S', '1n': 'L', '2': 'SN', '2n': 'LN', '2r': 'SN', '2rn': 'LN', '3': 'NC', '3n': 'NC',
                            '3tm': 'N','3tmn': 'N', '4': 'SNC', '4n': 'LNC', '4r': 'SNC', '4rn': 'LNC', '4t': 'SNCR', '4tn': 'LNCR',
                            '5': 'NC', '5n': 'NC', '6': 'NCR', '6n': 'NCR', '7': 'NC', '7n': 'NC', '8': 'NC',
                            '8n': 'NC', '9': 'SN', '9n': 'LN'}

dicionario_converte_copia = {0: 0, 1: 29, 2: 58, 3: 87, 4: 116, 5:145}
# --------------------------------
# programa principal
# path

extensao = ".png"
graus = "º"
print("Versão 1.4")
time.sleep(2)
# TODO: VERIFICAR SE A PLANILHA EXISTE, CASO CONTRARIO CRIAR PLANILHA COM A FUNÇÃO construir_planilha()

clima.construir_planilha(diretorio_planilha,'clima_tempo_python.xls')

read_planilha = xlrd.open_workbook(diretorio_planilha + 'clima_tempo_python.xls')
workbook_edit = copy(read_planilha)
w_sheet = workbook_edit.get_sheet(0)


for copia in range(5):

    json_clima_tempo = "erro"
    for i in lista_ids_cidades[0:10]:

        if copia == 0:
            json_clima_tempo = clima.req_clima_tempo(i, token0)
        else:
            json_clima_tempo = "erro"

        if (json_clima_tempo != "erro" and copia == 0):
            dados_importantes = clima.extrai_campos_importantes(json_clima_tempo,diretorio_json)

        else:
            print("----->>>>Excedeu o limite do dia<<<<-----")
            dados_importantes = clima.extrai_campos_importantes_arquivo(i,diretorio_json,dicionario_ids_cidades)

        print(
            'Cidade {0} Temperatura: {1} Icone: {2}'.format(dados_importantes[0], str(dados_importantes[1]) + graus,
                                                            caminho_icones + dados_importantes[2] + extensao))
        # GRAVANDO CONTEUDO NA PLANILHA
        # indice representa a linha da planilha
        indice = lista_ids_cidades.index(i) + 2 + dicionario_converte_copia[copia]

        print("Linha da planilha {0}".format(indice))
        w_sheet.write(indice - 1, 0, dados_importantes[0])
        w_sheet.write(indice - 1, 1, str(dados_importantes[1]) + graus)
        w_sheet.write(indice - 1, 2, caminho_icones + dados_importantes[2] + extensao)
        w_sheet.write(indice - 1, 3, dicionario_traduz_icones[dados_importantes[2]] + extensao)

    for i in lista_ids_cidades[10:20]:
        if copia == 0:
            json_clima_tempo = clima.req_clima_tempo(i, token0)
        else:
            json_clima_tempo = "erro"

        if (json_clima_tempo != "erro" and copia == 0):
            dados_importantes = clima.extrai_campos_importantes(json_clima_tempo,diretorio_json)

        else:
            print("----->>>>Excedeu o limite do dia<<<<-----")
            dados_importantes = clima.extrai_campos_importantes_arquivo(i,diretorio_json,dicionario_ids_cidades)

        print(
            'Cidade {0} Temperatura: {1} Icone: {2}'.format(dados_importantes[0], str(dados_importantes[1]) + graus,
                                                            caminho_icones + dados_importantes[2] + extensao))
        # GRAVANDO CONTEUDO NA PLANILHA
        indice = lista_ids_cidades.index(i) + 2 + dicionario_converte_copia[copia]
        print("Linha da planilha {0}".format(indice))
        w_sheet.write(indice - 1, 0, dados_importantes[0])
        w_sheet.write(indice - 1, 1, str(dados_importantes[1]) + graus)
        w_sheet.write(indice - 1, 2, caminho_icones + dados_importantes[2] + extensao)
        w_sheet.write(indice - 1, 3, dicionario_traduz_icones[dados_importantes[2]] + extensao)

    for i in lista_ids_cidades[20:]:
        if copia == 0:
            json_clima_tempo = clima.req_clima_tempo(i, token0)
        else:
            json_clima_tempo = "erro"

        if (json_clima_tempo != "erro" and copia == 0):
            dados_importantes = clima.extrai_campos_importantes(json_clima_tempo,diretorio_json)

        else:
            print("----->>>>Excedeu o limite do dia<<<<-----")
            dados_importantes = clima.extrai_campos_importantes_arquivo(i,diretorio_json,dicionario_ids_cidades)

        print(
            'Cidade {0} Temperatura: {1} Icone: {2}'.format(dados_importantes[0], str(dados_importantes[1]) + graus,
                                                            caminho_icones + dados_importantes[2] + extensao))
        # GRAVANDO CONTEUDO NA PLANILHA
        indice = lista_ids_cidades.index(i) + 2 + dicionario_converte_copia[copia]
        print("Linha da planilha {0}".format(indice))
        w_sheet.write(indice - 1, 0, dados_importantes[0])
        w_sheet.write(indice - 1, 1, str(dados_importantes[1]) + graus)
        w_sheet.write(indice - 1, 2, caminho_icones + dados_importantes[2] + extensao)
        w_sheet.write(indice - 1, 3, dicionario_traduz_icones[dados_importantes[2]] + extensao)

print("Atualizando Planilha")
workbook_edit.save(diretorio_planilha + 'clima_tempo_python.xls')
time.sleep(5)
print("Atualizando pagina de monitoração")
Gerador_html_clima_tempo.main()


# TODO:
# TODO:
