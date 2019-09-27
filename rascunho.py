import api_globo_poo
import dateutil.relativedelta
import datetime
import wget
import hashlib
import requests
import subprocess
import os,re
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
