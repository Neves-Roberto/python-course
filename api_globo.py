import requests
import json
from datetime import datetime
import hashlib


hoje = datetime.now()


hoje_formatado = str(hoje.year) + '-' + str(hoje.month) + '-' + str(hoje.day)
grant_type = 'password'
username = 'entregadigital.api'
password = 'Tri#01'
client_id = 'downloadapp'
client_secret = 'downloadsecret'
url_token = "https://api.tvglobo.com.br/integradorgmid/oauth/token"


def GetToken(grant_type='password', username='entregadigital.api', password='Tri#01', client_id='downloadapp',
             client_secret='downloadsecret', url_token="https://api.tvglobo.com.br/integradorgmid/oauth/token"):
    # Retorna o token valido e o type_token
    # solicitando token
    dados_acesso = {'grant_type': grant_type, 'username': username, 'password': password, 'client_id': client_id,
                    'client_secret': client_secret}
    request_token = requests.post(url_token, data=dados_acesso)

    # extraindo campos
    campo_json = json.loads(request_token.text)
    token = campo_json['access_token']
    tipo_token = campo_json['token_type']
    # returna uma lista
    return (token, tipo_token)


def GetMateriais(destino='SAN', idPlayers='1,2,3,4', statusDownload='', dataDe=hoje_formatado, dataAte=hoje_formatado,
                 idRequisicao='1', cdMateriais=[]):
    # destino padrao SAN [{"mnemonico":"SAN","nome":"SAN"}]
    # id dos servidores [{"id":1,"nome":"ADSTREAM"},{"id":2,"nome":"ADTOOX"},{"id":3,"nome":"VATI"},{"id":4,"nome":"ZARPA"}]

    # data no formato AAAA-MM-DD
    # data no formato AAAA-MM-DD
    # inteiro

    token, tipo_token = GetToken()

    url_materiais = 'https://api.tvglobo.com.br/integradorgmid/api/rest/v3/materiais-cloud?'
    dados_materiais = {'destino': destino, 'idPlayers': idPlayers, 'statusDownload': statusDownload, 'dataDe': dataDe,
                       'dataAte': dataAte, 'cdMateriais[]': cdMateriais}
    # dados_materiais = {'destino':destino,'idPlayers':idPlayers,'statusDownload':statusDownload,'codMaterial':codMaterial}
    dados_headers = {'accept': 'application/json', 'idRequisicao': idRequisicao,
                     'authorization': tipo_token + ' ' + token}

    request_materiais = requests.get(url=url_materiais, params=dados_materiais, headers=dados_headers)
    # print(request_materiais.url)
    materiais_json = json.loads(request_materiais.text)
    # retorna um Json com a lista de materiais
    # TODO fazer verificação de resposta do retorno, se é 200 para liberar a resposta em json, caso contrario retornar -1
    return (materiais_json)


def GetLimites(idRequisicao='1'):
    url_limites = 'https://api.tvglobo.com.br/integradorgmid/api/rest/v3/materiais-cloud/limite-registros-exibido'
    token, tipo_token = GetToken()
    dados_headers = {'accept': 'application/json', 'idRequisicao': idRequisicao,
                     'authorization': tipo_token + ' ' + token}
    request_limites = requests.get(url=url_limites, headers=dados_headers)
    limites_json = json.loads(request_limites.text)
    return (limites_json)


def GetDestinos(idRequisicao='1'):
    url_destinos = 'https://api.tvglobo.com.br/integradorgmid/api/rest/v2/destinos'
    token, tipo_token = GetToken()
    dados_headers = {'accept': 'application/json', 'idRequisicao': idRequisicao,
                     'authorization': tipo_token + ' ' + token}
    request_destinos = requests.get(url=url_destinos, headers=dados_headers)
    destinos_json = json.loads(request_destinos.text)
    return (destinos_json)


def GetPlayers(idRequisicao='1'):
    url_players = 'https://api.tvglobo.com.br/integradorgmid/api/rest/v2/players'
    token, tipo_token = GetToken()
    dados_headers = {'accept': 'application/json', 'idRequisicao': idRequisicao,
                     'authorization': tipo_token + ' ' + token}
    request_players = requests.get(url=url_players, headers=dados_headers)
    players_json = json.loads(request_players.text)
    return (players_json)


def GetEnderecos(idRequisicao='1', idMateriais=''):
    url_enderecos = "https://api.tvglobo.com.br/integradorgmid/api/rest/v3/materiais-cloud/enderecos?idMateriais[]=" + idMateriais
    token, tipo_token = GetToken()
    dados_headers = {'accept': 'application/json', 'idRequisicao': idRequisicao,
                     'authorization': tipo_token + ' ' + token}
    request_enderecos = requests.get(url=url_enderecos, headers=dados_headers)
    enderecos_json = json.loads(request_enderecos.text)
    return (enderecos_json)


def DownloadMaterial(idMaterial, nomeArquivo, md5):
    print("Iniciando Download do arquvo ", nomeArquivo)
    url = GetEnderecos(idMateriais=idMaterial)['enderecos'][0]
    print(url)
    r = requests.get(url,
                     verify='C:\\Program Files\\Microsoft Office\\Office14\\Groove\\Certificates\\Verisign\\Components\\VeriSign_Class_3_Code_Signing_2001-4_CA.cer')
    with open(nomeArquivo, "wb") as code:
        code.write(r.content)

    print("Download Finalizado do arquvo ", nomeArquivo)
    print("Checando integridade do arquivo")

    hasher = hashlib.md5()
    with open(nomeArquivo, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
    if (hasher.hexdigest() == md5):
        print("Material OK")
    else:
        print("Material Com Problema, Refazer Download")

def GerarPaginaEstrutura():
    #TODO montar função de gera arquivo html contendo conteudo da pagina equivalente da consulta realizada
    itens = ('ID_MATERIAL', 'PTO_VENDA', 'COD_MATERIAL', 'PLAYER', 'DATA_ENVIO', 'TITULO', 'STATUS_DOWNLOAD', 'NOME_ARQUIVO', 'MD5','URL_DOWNLOAD')

    with open('teste.html', "w") as pagina:
        hora_atual = hoje_formatado + ' ' + str(hoje.hour) + ':' + str(hoje.minute) + ':' + str(hoje.second)
        pagina.write('''<!DOCTYPE html>
        <html>
        <head>
        <style>
        table, td, th, tfoot {border:solid 1px #000; padding:5px;}
        th {background-color:#999;}
        caption {font-size:x-large;}
        colgroup {background:#F60;}
        .coluna1 {background:#F66;}
        .coluna2  {background:#F33;}
        .coluna4  {background:#F99;}
        .coluna5  {background:#F99;}
        .coluna6  {background:#F99;}
        .coluna7  {background:#F99;}
        .coluna8  {background:#F99;}
        </style>
            </head>
                <body>
                <h1> LISTA MATERIAIS OPEC - API GLOBO </h1>
                <h3>Ultima atualização ''' + hora_atual + '''</h3>
                <table>
                <colgroup span=3></colgroup>
                <tr>
                ''')
        print('''<!DOCTYPE html>
        <html>
        <head>
        <style>
        table, td, th, tfoot {border:solid 1px #000; padding:5px;}
        th {background-color:#999;}
        caption {font-size:x-large;}
        colgroup {background:#F60;}
        .coluna1 {background:#F66;}
        .coluna2  {background:#F33;}
        .coluna3  {background:#F99;}
        </style>
            </head>
                <body>
                <h1> LISTA MATERIAIS OPEC - API GLOBO </h1>
                <h3>Ultima atualização ''' + hora_atual + '''</h3>
                <table>
                <colgroup span=3></colgroup>
                <tr>
                ''')
        for item in itens:
            pagina.write("            <th>{0}</th>".format(item))
            print("            <th>{0}</th>".format(item))

        pagina.write('''   </tr>
        <tr>''')
        print('''   </tr>''')
        
        


def GerarPaginaCorpo(iten,AtivarLinha,DesativaLinha):
    with open('teste.html', "a") as pagina:
        if AtivarLinha:
            # inserindo linha
            pagina.write("<tr>")
            print("<tr>")


        # inserindo dados
        pagina.write("            <td>{0}</td>".format(iten))
        print("            <td>{0}</td>".format(iten))

        if DesativaLinha:
            # fechando a linha
            pagina.write('''
                    </tr>''')
            print('''</tr>''')
            pagina.close()

def GerarPaginaFim():
    with open('teste.html', "a") as pagina:
        pagina.write('''
                  </table>
                  </body>
                </html> ''')
        print('''

                        </table>
                        </body>
                        </html> ''')
        pagina.close()


def GerarListaMateriais(Materiais=[]):
    GerarPaginaEstrutura()
    #dataDe='2018-11-29'
    ListaMateriais = GetMateriais(cdMateriais=Materiais)
    # print(type(ListaMateriais))

    QuantidadeMateriais = len(ListaMateriais)
    # print(ListaMateriais)
    # print(QuantidadeMateriais)
    Ativar = True
    Desativar= False
    for listaMaterial in ListaMateriais:
        QuantidadeMateriais = QuantidadeMateriais - 1
        # print(listaMaterial)
        # print("------------")
        # listaMaterial.keys()
        # for iten in ('idMaterial','ptoVenda','codMaterial','cliente','agencia','player','dataEnvio','titulo','statusDownload','nomeArquivo','md5'):
        #	print(iten, end=" | ")
        # print()

        for iten in ('idMaterial', 'ptoVenda', 'codMaterial', 'player', 'dataEnvio', 'titulo', 'statusDownload', 'nomeArquivo','md5'):
            #espacoPadrao = 2
            # 1 espaço
            print(listaMaterial[iten])
            GerarPaginaCorpo(listaMaterial[iten], AtivarLinha = Ativar, DesativaLinha = Desativar)
            Ativar = False
            if iten == 'idMaterial':
                print(" ", end='')
                print(listaMaterial[iten], end=" | ")
                DesativaLinha = False
            if iten == 'ptoVenda':
                print(" ", end='')
                print(listaMaterial[iten], end=" |")
            if iten == 'codMaterial':
                # print(" ",end='')
                # print(listaMaterial[iten], end=" | ")
                for a in range(8 - len(str(listaMaterial[iten]))):
                    print(" ", end='')
                print(listaMaterial[iten], end=" | ")
            if iten == 'player':
                for i in range(8 - len(listaMaterial[iten])):
                    print(" ", end='')
                print(listaMaterial[iten], end=" | ")
            if iten == 'dataEnvio':
                print(" ", end='')
                print(listaMaterial[iten], end=" | ")
            if iten == 'titulo':
                for i in range(30 - len(listaMaterial[iten])):
                    print(" ", end='')
                print(listaMaterial[iten], end=" | ")
            if iten == 'statusDownload':
                for i in range(11 - len(listaMaterial[iten])):
                    print(" ", end='')
                print(listaMaterial[iten], end=" | ")
            if iten == 'nomeArquivo':
                for i in range(40 - len(listaMaterial[iten])):
                    print(" ", end='')
                print(listaMaterial[iten], end=" |")
            if iten == 'md5':
                print(" ", end='')
                print(listaMaterial[iten], end="| ")
                # time.sleep(3)
                try:
                    url = GetEnderecos(idMateriais=str(listaMaterial['idMaterial']))['enderecos'][0]
                    print(url)
                    GerarPaginaCorpo("<a href=" + url + ">"+ listaMaterial['nomeArquivo'] + "</a>", AtivarLinha=Ativar, DesativaLinha=Desativar)
                except:
                    print("Não foi possivel obter a URL de Download")
                    GerarPaginaCorpo("Não foi possivel obter a URL de Download", AtivarLinha=Ativar,DesativaLinha=Desativar)
                #print(QuantidadeMateriais, end="")
                #Desativar = True

                print()
        Ativar = True
    GerarPaginaFim()


                #return(iten,QuantidadeMateriais)
    # print("Processo de Download")
    # DownloadMaterial(str(listaMaterial['idMaterial']),listaMaterial['nomeArquivo'],listaMaterial['md5'])


# print(request_token.status_code)
# print(request_token.text)
# print(campo_json)
# print(type(campo_json))
# print(campo_json['access_token'])
# print(campo_json['token_type'])


# print(request_materiais.status_code)
# print(request_materiais.text)
# print(materiais_json)
# materiais_json = GetMateriais(dataDe='2018-11-29')
# print(len(materiais_json))
# print(materiais_json)
# print(materiais_json[0].keys())
# print(len(materiais_json[0].keys()))


# print(request_limites.status_code)
# print(request_limites.text)
# print(limites_json)


# print(request_destinos.status_code)
# print(request_destinos.text)
# print(destinos_json)


# players_json = GetPlayers()
# print(request_players.status_code)
# print(request_players.text)
# print(len(players_json))
# print(players_json[0]['nome'])


# enderecos_json = GetEnderecos(idMateriais='278820')

# print(request_enderecos.status_code)
# print(request_enderecos.text)
# print(enderecos_json['enderecos'][0])
# Materiais = ['143435']
#DataInicio = str(input("Digite a data de inicio [AAAA-MM-DD] [OPCIONAL]"))
#DataFim = str(input("Digite a data de fim [AAAA-MM-DD] [OPCIONAL]"))
#CodigoMaterial = [str(input("Digite o Codigo de Material separado por virgula: "))]
#print(type(DataInicio),type(DataFim),type(CodigoMaterial))
#DataInicio,DataFim,
#GerarListaMateriais()
