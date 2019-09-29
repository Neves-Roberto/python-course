import os,re
import time
import datetime
import dateutil.relativedelta


def lista_arquivos(diretorio,extensao='mxf'):

    pattern = '.*'
    pasta = diretorio# diretorio onde localiza os arquivos .extensao
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    lista_arquivos_extensao = [re.findall(pattern,arq) for arq in arquivos if arq.lower().endswith(extensao.lower())]  # lista com todos os arquivos .extensao no diretorio
    return lista_arquivos_extensao



path = 'Y:\\SISCOM\\'
path_api = 'C:\\Users\\projetos\\PycharmProjects\\python-course\\Comerciais_Api_globo\\'

DIAS = 110 # arqvuivos com mais de X dias serao deletados

data_de = datetime.datetime.strptime(str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day), "%Y-%m-%d")
novo_data_de = data_de - dateutil.relativedelta.relativedelta(days=DIAS)
data = str(novo_data_de.year) + "-" + str(novo_data_de.month) + "-" + str(novo_data_de.day)
print(data)
s = data
timestamp = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple())
print(timestamp)
contador = 0
for arquivo in lista_arquivos(path):

    if arquivo:
        Seconds = os.path.getctime(arquivo[0])
        if Seconds <= timestamp:
            mensagem = 'O arquivo {0} foi deletado com data de criacao em {1}\n'.format(arquivo[0], time.ctime(Seconds))
            print(mensagem)
            contador += 1
            #os.remove(arquivo[0])
            arquivo_log = open(path_api + 'log_download_api.txt', 'a+')
            arquivo_log.write(mensagem)
            #arquivo_log.close()
print(contador)
arquivo_log = open(path_api + 'log_download_api.txt', 'a+')
arquivo_log.write('Apagado {0} arquivos com mais de {1} dias de criacao\n'.format(contador,DIAS))
arquivo_log.close()