
import os,re
import subprocess



def lista_arquivos(diretorio,extensao='mxf'):
    #pattern = '.*\(\d\).*'
    pattern = '.*'
    pasta = diretorio# diretorio onde localiza os arquivos .extensao
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    lista_arquivos_extensao = [re.findall(pattern,arq) for arq in arquivos if arq.lower().endswith(extensao.lower())]  # lista com todos os arquivos .extensao no diretorio
    return lista_arquivos_extensao

path = 'Y:\\SISCOM\\'
#path = 'C:\\Users\\projetos\\Downloads\\MediaInfo_CLI_19.09_Windows_i386\\'
path_api = 'C:\\Users\\projetos\\PycharmProjects\\python-course\\Comerciais_Api_globo\\arquivos_json\\'

for arquivo in lista_arquivos(path):
    nomeArquivo = arquivo[0].replace(path, '').replace('.mxf', '')
    string = "\""+ arquivo[0]+"\""
    print(string)
    subprocess.call("C:\\Users\\projetos\\Downloads\\MediaInfo_CLI_19.09_Windows_i386\\MediaInfo {0} --Output=JSON --LogFile={1}.json".format(string, path_api+nomeArquivo.replace(' ','_')), shell=False)
