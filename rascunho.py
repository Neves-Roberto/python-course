import api_globo_poo
import dateutil.relativedelta
import datetime
import wget
import hashlib
import requests
import subprocess
import os,re
import subprocess
import json

dict = {'idMaterial': 337773, 'idMaterialParceiro': '1213654', 'ptoVenda': 'PES', 'codMaterial': 254057, 'cliente': 'TRE', 'idPlayer': 4, 'player': 'ZARPA', 'dataEnvio': '2019-03-29', 'primeiraVeiculacao': '24/09/2019 FATI', 'titulo': 'BIOMETRIA N1 - SP', 'duracao': 30, 'statusDownload': 'emAndamento', 'exibidoras': ['SAN'], 'nomeArquivo': '254057_BIOMETRIA N1 - SP.MXF', 'tamArquivo': 281.11142, 'md5': '1b47958bc24ab4e773df954e5dcf8c27'}
'''
print(dict['idMaterial'])
print(dict['idMaterialParceiro'])
print(dict['ptoVenda'])
print(dict['codMaterial'])
print(dict['cliente'])
print(dict['idPlayer'])
print(dict['dataEnvio'])
print(dict['primeiraVeiculacao'])
print(dict['titulo'])
print(dict['duracao'])
print(dict['statusDownload'])
print(dict['exibidoras'])
print(dict['nomeArquivo'].replace(' ','_'))
print(dict['tamArquivo'])
print(dict['md5'])
'''



opec = api_globo_poo.apiGlobo()
'''
#print(opec.GetMateriais(cdMateriais=[]))
lista_ok = []
arq_lista_ok = open('listadownload_ok.txt','r')
for linha in arq_lista_ok:
    lista_ok.append(int(linha.replace('\n','')))
print(lista_ok)

data_de = datetime.datetime.strptime(str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day), "%Y-%m-%d")
novo_data_de = data_de - dateutil.relativedelta.relativedelta(days=1)
data = str(novo_data_de.year) + "-" + str(novo_data_de.month) + "-" + str(novo_data_de.day)
lista_material_opec = enumerate(opec.GetMateriais(dataDe=[data]))
for num, material in lista_material_opec:

    if material['codMaterial'] in lista_ok:
        print(str(num) + ' ' + str(material['codMaterial']) + " EXISTE " )
    else:
        print(str(num) + ' ' + str(material['codMaterial']) + " NAO EXISTE ")

'''
'''
#wget.download(url)
#https://gw.casavaticano.com.br/index.php/materialEnderecos/1084210?access_token=b0yAKp1xwoxDbHy7fbUIlC9gh1KI6nSY1VQocvht
id = '440211'
url = str(opec.GetEnderecos('1',id)['enderecos'][0])
endereco ='C:\\Users\\dkscr\\PycharmProjects\\python-course\\teste_.mxf'
def baixar_arquivo(url, endereco):
    resposta = requests.get(url, stream=True, verify=False) #AQUI
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
                for parte in resposta.iter_content(chunk_size=256): #AQUI TBM
                    novo_arquivo.write(parte)
        print("Download finalizado. Arquivo salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()
baixar_arquivo(url,endereco)

r = subprocess.call("curl --cacert cacert.pem -L --cookie-jar ./somefile -d \"email=jose.menezes@tvtribuna.com&password=TVtribuna.18\" https://tvs.climatempo.com.br/auth",
    shell=False)
print('Efetuando Autenticação ...')
arquivo_log.write('Efetuando Autenticação - {0}\n'.format(datetime.now()))
r = subprocess.call(
    "curl --cacert cacert.pem -L --cookie ./somefile \"https://tvs.climatempo.com.br/download?t=c2F0ZWxsaXRl&r=YnI=\" --output PREVISAO_DO_DIA\satbra.GIF",
    shell=False)
'''
"""lista_material_opec = opec.GetMateriais(dataDe=['2019-09-26'], cdMateriais=['386114'])

for material in lista_material_opec:
    data_log = datetime.datetime.strptime(str(datetime.datetime.now().day) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().hour) + '-' + str(datetime.datetime.now().minute) + '-' + str(datetime.datetime.now().second),"%d-%m-%Y-%H-%M-%S")
    print(type(str(material['codMaterial'])))
    print(str(data_log)  + " CODIGO " + str(material['codMaterial']))

print('Abrindo arquivo de log')
arquivo_log = open(path_api + 'log_download_api.txt', 'a')
print(path_api + 'log_download_api.txt')
data_log = datetime.datetime.strptime(
    str(datetime.datetime.now().day) + '-' + str(datetime.datetime.now().month) + '-' + str(
        datetime.datetime.now().year) + '-' + str(datetime.datetime.now().hour) + '-' + str(
        datetime.datetime.now().minute) + '-' + str(datetime.datetime.now().second),
    "%d-%m-%Y-%H-%M-%S")
arquivo_log.write(str(data_log) + ' CODIGO ' + material[
    'codMaterial'] + ' EFETUADO DOWNLOAD ALTERNATIVO DO ARQUIVO ' + nomeMaterial + '\n')
arquivo_log.close()
print('Arquivo fechado log')"""

"""path = 'C:\\Users\\dkscr\\PycharmProjects\\python-course\\SISCOM\\'
extensao = 'mxf'
def lista_arquivos(diretorio,extensao):
    pattern = '^\d+'
    pasta = diretorio# diretorio onde localiza os arquivos .extensao
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    lista_arquivos_extensao = [re.findall(pattern,arq.replace(path,''))[0] for arq in arquivos if arq.lower().endswith(extensao.lower())]  # lista com todos os arquivos .extensao no diretorio
    return lista_arquivos_extensao

print(lista_arquivos(path,extensao))"""


print("{\"DIAS\": 1, \"TDLY\": 120 }\n")

import smtplib
#from email.mime.text import MIMEText
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# conexão com os servidores do google
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
# username ou email para logar no servidor
username = 'dkscript@gmail.com'
password = 'desptro007'

from_addr = 'dkscript@gmail.com'
to_addrs = ['flavio.santos@tvtribuna.com']

# a biblioteca email possuí vários templates
# para diferentes formatos de mensagem
# neste caso usaremos MIMEText para enviar
# somente texto
message = MIMEMultipart()
message['subject'] = 'Hello'
message['from'] = from_addr
message['to'] = ', '.join(to_addrs)
# Anexa a imagem
imgFilename = 'Ó o auê aí, ô.jpg' # Repare que é diferente do nome do arquivo local!
with open('img.jpg', 'rb') as f:
    msgImg = MIMEImage(f.read(), name=imgFilename)
message.attach(msgImg)


with open('log_download_api_4-10-2019.txt', 'r') as f:
    msgImg = MIMEText(f.read(),_subtype='txt')
    msgImg.add_header('content-disposition', 'attachment', filename='log.txt')
message.attach(msgImg)

"""
# Anexa o corpo do texto
msgText = MIMEText('<b>{}</b><br><img src="cid:{}"><br>'.format(body, imgFilename), 'html')
message.attach(msgText)
"""

# conectaremos de forma segura usando SSL
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
# para interagir com um servidor externo precisaremos
# fazer login nele
server.login(username, password)
server.sendmail(from_addr, to_addrs, message.as_string())
server.quit()


#path = 'C:\\Users\\projetos\\PycharmProjects\\python-course\\mxf\\'
path = 'Y:\\SISCOM\\'
path_api = 'C:\\Users\\projetos\\PycharmProjects\\python-course\\Comerciais_Api_globo\\arquivos_json\\'


'''
try:
    config_arq = open(path_api + 'config.json', 'r+')
    config_json = json.loads(config_arq.readlines()[0])
    config_arq.close
    print(config_json)
except FileNotFoundError:
    print("Arquivo de configuração não encontrado!")
    print("Aplicando valores padroes:")
    DIAS = 0
    TDLY = 120
    print("Criando arquivo de configuracao padrao")
    arq_config = open(path_api + 'config.json', 'w')
    arq_config.write("{\"DIAS\": 0, \"TDLY\": 120 }\n")
    arq_config.write("#Arquivo de configuracao do download_api_globo\n")
    arq_config.write("#Parametro DIAS, quantidade de dias que deseja manter atualizado, 0 eh o mesmo dias, 1 eh o dia atual mais 1 (um) ...\n")
    arq_config.write("#Parametro TDLY eh o tempo de delay para a nova verificação em segundos.\n")
    arq_config.close
except IndexError:
    print('fora do indice')
    DIAS = 0
    TDLY = 120
    
       
'''
'''
def extrai_campos_importantes_arquivo_json(arquivo_json_diretorio):
    # retorna lista contendo o que é importante
    arquivo_json = open(arquivo_json_diretorio, 'rt')
    print(arquivo_json)
    dict_arquivo_json = json.loads(arquivo_json)
    print(dict_arquivo_json)
    arquivo_json.close()
    return dict_arquivo_json
#(teste['name'], ceil(teste['data']['temperature']), teste['data']['icon'],teste['data']['humidity'],teste['data']['condition'])

def lista_arquivos(diretorio,extensao='mxf'):
    #pattern = '.*\(\d\).*'
    pattern = '.*'
    pasta = diretorio# diretorio onde localiza os arquivos .extensao
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    lista_arquivos_extensao = [re.findall(pattern,arq) for arq in arquivos if arq.lower().endswith(extensao.lower())]  # lista com todos os arquivos .extensao no diretorio
    return lista_arquivos_extensao


#print(lista_arquivos(path_api,'json'))

#for arquivo in lista_arquivos(path_api,'json'):
#    print(arquivo[0])
#arquivo_json_diretorio = 'C:\\Users\\projetos\\PycharmProjects\\python-course\\Comerciais_Api_globo\\AMOSTRA_PCM_BIG_LITTLE\\CH_MC_MESTRE_AVILLEZ_DIA_10_B_SHARE.json'
arquivo_json_diretorio = 'C:\\Users\\projetos\\PycharmProjects\\python-course\\Comerciais_Api_globo\\arquivos_json\\247631_METAMORPHOSIS_1_DE_5.MXF.json'


with open(arquivo_json_diretorio) as file_data:
    data = file_data.readlines()
print(data)
arquivo_json = ''
for item in (data):
    arquivo_json += item
#print(arquivo_json)
extraido_json = json.loads(arquivo_json)
#print(extraido_json)
print(extraido_json['media']['track'][1]['@type'])
print((extraido_json['media']['track'])[2]['Format_Settings_Endianness'])
print(len(extraido_json['media']['track']))

for item in range(len(extraido_json['media']['track'])):
    print(extraido_json['media']['track'][item]['@type'])

#print(extraido_json['media']['track'])

def temCloseCaption(arquivo_json):
    with open(arquivo_json) as file_data:
        data = file_data.readlines()

    arquivo_json = ''
    for item in (data):
        arquivo_json += item
    extraido_json = json.loads(arquivo_json)
    temcc = False

    for item in range(len(extraido_json['media']['track'])):
        if extraido_json['media']['track'][item]['@type'] == 'Text':
            temcc = True
    return temcc

print(temCloseCaption(arquivo_json_diretorio))
'''
'''
arquivo_json = open(arquivo_json_diretorio, 'rt')
print(arquivo_json)
dict_arquivo_json = json.loads(arquivo_json.readlines())
print(dict_arquivo_json)
arquivo_json.close()
#dict_arquivo_json
'''



"""
def lista_arquivos(diretorio,extensao='mxf'):
    pasta = diretorio# diretorio onde localiza os arquivos .extensao
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    lista_arquivos_extensao = [arq for arq in arquivos if arq.lower().endswith(extensao.lower())]  # lista com todos os arquivos .extensao no diretorio
    return lista_arquivos_extensao
"""
'''
#data = '2019-09-27'
lista_arquivos_diretorio =lista_arquivos(path)
print(lista_arquivos_diretorio)
tamanho = len(lista_arquivos_diretorio)
print('tamanho da lista ' + str(tamanho))
for lista in lista_arquivos_diretorio:
    if lista:
        print(lista[0])
        os.remove(lista[0])
        print('removendo ...')
'''

'''
from pathlib import Path

data_criacao = lambda f: f.stat().st_ctime
data_modificacao = lambda f: f.stat().st_mtime

directory = Path(path)
files = directory.glob('*.mxf')
sorted_files = sorted(files, key=data_criacao, reverse=True)

print(data_modificacao)
#for f in sorted_files:
#    print(f)
'''
"""
import os
import time

DIAS = 100 # arqvuivos com mais de X dias serao deletados

data_de = datetime.datetime.strptime(str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day), "%Y-%m-%d")
novo_data_de = data_de - dateutil.relativedelta.relativedelta(days=DIAS)
data = str(novo_data_de.year) + "-" + str(novo_data_de.month) + "-" + str(novo_data_de.day)
print(data)
#s = "2019-06-07"
s = data
timestamp = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple())
print(timestamp)
contador = 0
for arquivo in lista_arquivos(path):

    if arquivo:

        #print(arquivo[0])

        #nome_arquivo = raw_input('digite o nome do arquivo: ')
        Seconds = os.path.getctime(arquivo[0])
        if Seconds <= timestamp:
            print('O arquivo foi criado em %s' %time.ctime(Seconds))
            contador += 1
print(contador)
"""




"""
arquivo = 'Y:\\SISCOM\\183540_ARRIZO5_INSTITUCIONAL_0105.mxf'

print(os.path.getsize(arquivo))
#print(time.ctime(os.path.getatime(arquivo)))
print(os.path.getctime(arquivo))
print(os.path.getmtime(arquivo))
nomeArquivo = arquivo.replace('Y:\\SISCOM\\','').replace('.mxf','')
print(subprocess.call("C:\\Users\\projetos\\Downloads\\MediaInfo_CLI_19.09_Windows_i386\\MediaInfo {0} --Output=JSON --LogFile={1}.json".format(arquivo,nomeArquivo),shell=False))

print()

"""


"""
import time
import datetime
#s = "01/12/2011"
s = "2019/09/29 00:00:00"
print(time.mktime(datetime.datetime.strptime(s, "%Y/%m/%d %H:%M:%S").timetuple()))
s = "2019/09/25 00:00:00"
print(time.mktime(datetime.datetime.strptime(s, "%Y/%m/%d %H:%M:%S").timetuple()))
'''
#TODO: LISTAR TODOS OS ARQUVIVOS QUE TENHAM DATA MENOR QUE A DATA CITADA



'''
a = 900
b = 910
print(a,b)
while (a <= tamanho) or (b <= tamanho):


    lista_material_opec = opec.GetMateriais(cdMateriais=lista_arquivos_diretorio[a:b])
    dicionario_codigoMat_Md5 = {}
    contador = 0
    for material in lista_material_opec:
        dicionario_codigoMat_Md5.update({lista_arquivos_diretorio[contador]:material['md5']})
        contador += 1
        nomeMaterial = material['nomeArquivo']#.replace(' ', '_')
        print(nomeMaterial)
        try:

            arquivo = open(path + nomeMaterial, 'rb').read()
            md5_arquivo = hashlib.md5(arquivo)
            md5_final = md5_arquivo.hexdigest()
            if str(md5_final) == str(material['md5']):
                print('CONFERE  ' + nomeMaterial)
            else:
                print('DIVERGENTE ---------------' + nomeMaterial)
                arq_config = open(path_api + 'divergencia.txt', 'a+')
                arq_config.write(nomeMaterial)
                arq_config.close
        except FileNotFoundError:
            print("Procurar alternativa ")
            try:
                nomeMaterial = material['nomeArquivo'].replace(' ', '_')
                arquivo = open(path + nomeMaterial, 'rb').read()
                md5_arquivo = hashlib.md5(arquivo)
                md5_final = md5_arquivo.hexdigest()
                if str(md5_final) == str(material['md5']):
                    print('CONFERE ALTERNATIVA ' + nomeMaterial)
                else:
                    print('DIVERGENTE ALTERNATIVA---------------' + nomeMaterial)
                    arq_config = open(path_api + 'divergencia.txt', 'a+')
                    arq_config.write(nomeMaterial)
                    arq_config.close
            except:
                print("Nao foi possivel")
                




    a += 10
    b += 10
    print(a,b)
"""

"""
config_arq = open(path_api + 'arq_config.json', 'r+')
print(config_arq)
config_json = json.loads(config_arq.readlines()[0])
print(config_json)
config_arq.close
print(config_json)
"""

'''
except FileNotFoundError:
    print("Arquivo de configuração não encontrado!")
    print("Aplicando valores padroes:")
    DIAS = 60
    TDLY = 120
    print("Criando arquivo de configuracao padrao")
    config_arq = open(path_api + 'arq_config.json', 'w+')
    config_arq.write("{\"DIAS\": 60, \"TDLY\": 120 }\n")
    config_arq.write("#Arquivo de configuracao do download_api_globo\n")
    config_arq.write(
        "#Parametro DIAS, quantidade de dias que deseja manter atualizado, 0 eh o mesmo dias, 1 eh o dia atual mais 1 (um) ...\n")
    config_arq.write("#Parametro TDLY eh o tempo de delay para a nova verificação em segundos.\n")
    config_arq.close


except IndexError:
    print('fora do indice')
    DIAS = 60
    TDLY = 120
except json.decoder.JSONDecodeError:
    DIAS = 60
    TDLY = 120
    print('erro de decode json')

else:
    # Atualizando Variaveis
    DIAS = int(config_json['DIAS'])
    TDLY = int(config_json['TDLY'])

'''