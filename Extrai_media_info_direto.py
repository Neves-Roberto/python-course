
import os,re
import subprocess
import json

def checa_pcm(arquivo_json):

    extraido_json = json.loads(arquivo_json)

    return extraido_json['media']['track'][2]['Format_Settings_Endianness']

def temCloseCaption(arquivo_json):

    extraido_json = json.loads(arquivo_json)
    temcc = False

    for item in range(len(extraido_json['media']['track'])):
        if extraido_json['media']['track'][item]['@type'] == 'Text':
            temcc = True
    return temcc

def lista_arquivos(diretorio,extensao='mxf'):
    #pattern = '.*\(\d\).*'
    pattern = '.*'
    pasta = diretorio# diretorio onde localiza os arquivos .extensao
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    lista_arquivos_extensao = [re.findall(pattern,arq) for arq in arquivos if arq.lower().endswith(extensao.lower())]  # lista com todos os arquivos .extensao no diretorio
    return lista_arquivos_extensao

path = 'Y:\\SISCOM\\'
#path = 'Y:\\'
#path = 'C:\\Users\\projetos\\PycharmProjects\\python-course\\Comerciais_Api_globo\\AMOSTRA_PCM_BIG_LITTLE\\'
#path = 'C:\\Users\\projetos\\Downloads\\MediaInfo_CLI_19.09_Windows_i386\\'
#path_api = 'C:\\Users\\projetos\\PycharmProjects\\python-course\\Comerciais_Api_globo\\arquivos_json\\'
path_api = 'C:\\Users\\projetos\\PycharmProjects\\python-course\\Comerciais_Api_globo\\AMOSTRA_PCM_BIG_LITTLE\\'

for arquivo in lista_arquivos(path):
    nomeArquivo = arquivo[0].replace(path, '').replace('.mxf', '')
    string = "\""+ arquivo[0]+"\""
    print(string)
    texto_json = subprocess.getoutput("C:\\Users\\projetos\\Downloads\\MediaInfo_CLI_19.09_Windows_i386\\MediaInfo {0} --Output=JSON ".format(string, path_api+nomeArquivo.replace(' ','_')))
    if temCloseCaption(texto_json):
        print("tem cc")
    else:
        print("nao tem cc")
    print(checa_pcm(texto_json))



