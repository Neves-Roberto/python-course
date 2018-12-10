from math import ceil
import json
import requests
from xlwt import Workbook

diretorio_json = ""
diretorio_planilha = ""
caminho_icones = ""

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

def req_clima_tempo(ids, token):
    r = requests.get(
        'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{0}/current?token={1}'.format(ids, token))
    if (r.status_code == 200):
        # conexao ok, retorna json da cidade consultada
        return r.text
    else:
        return "erro"


def extrai_campos_importantes(json_id,diretorio):
    # retorna lista contendo o que é importante
    if (json_id != "erro"):
        teste = json.loads(json_id)
        arquivo_json = open(diretorio + '{0}.json'.format(teste['name']), 'w')
        arquivo_json.write(json_id)
        arquivo_json.close()
        return (teste['name'], ceil(teste['data']['temperature']), teste['data']['icon'])
    else:
        return "erro"



def extrai_campos_importantes_arquivo(json_id, diretorio, dicionario):
    # retorna lista contendo o que é importante
    cidade_json = diretorio + '{0}.json'.format(dicionario[json_id])
    arquivo_json = open(cidade_json, 'rt')
    teste = json.loads(arquivo_json.readlines()[0])
    arquivo_json.close()
    return (teste['name'], ceil(teste['data']['temperature']), teste['data']['icon'],teste['data']['humidity'],teste['data']['condition'])


def construir_planilha(diretorio,nomeArquivo):
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
    workbook_build.save(diretorio + nomeArquivo)

