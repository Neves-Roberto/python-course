import os,re


path = 'Y:\\SISCOM\\'
path_api = 'C:\\Users\\projetos\\PycharmProjects\\python-course\\Comerciais_Api_globo\\'


def lista_arquivos(diretorio,extensao='mxf'):
    pattern = '.*\(\d\).*'
    pasta = diretorio# diretorio onde localiza os arquivos .extensao
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    lista_arquivos_extensao = [re.findall(pattern,arq) for arq in arquivos if arq.lower().endswith(extensao.lower())]  # lista com todos os arquivos .extensao no diretorio
    return lista_arquivos_extensao

lista_arquivos_diretorio =lista_arquivos(path)
print(lista_arquivos_diretorio)
tamanho = len(lista_arquivos_diretorio)
print('tamanho da lista ' + str(tamanho))
for lista in lista_arquivos_diretorio:
    if lista:
        print(lista[0])
        os.remove(lista[0])
        print('removendo ...')