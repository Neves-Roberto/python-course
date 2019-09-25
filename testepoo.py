#criancao de classes em poo e heranca
import api_globo_poo
import wget
import hashlib
import dateutil.relativedelta
import datetime

def insereListaOk(idMaterial):
    pass

def insereListaNaoOk(idMaterial):
    pass


#path = 'C:\\Users\\projetos\\PycharmProjects\\python-course\\mxf\\'
#path = 'Y:\\SISCOM\\siscom_Teste\\'
path = ''



#wget.download('https://a5.adstream.com/globo/api/materiais/5d3b5012b9fc6651dee0fe98-RJP/download?IDRequisicao=126072019181100&access_token=83c5d7b0291f8ea783e40118d21684adaa4e5913','teste.mxf', bar=bar_custom)

data_de = datetime.datetime.strptime(str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day), "%Y-%m-%d")
novo_data_de = data_de - dateutil.relativedelta.relativedelta(days=0) # Quantidade de dias da atualizacao
data = str(novo_data_de.year) + "-" + str(novo_data_de.month) + "-" + str(novo_data_de.day)



opec = api_globo_poo.apiGlobo()



for material in opec.GetMateriais(dataDe=[data]):
    print(material)
    nomeMaterial = material['nomeArquivo'].replace(' ','_') # retira os espacos do nome do arquivo, substitui por underline
    #print(material['codMaterial'])
    md5_original = material['md5']
    #print(str(material['codMaterial']))

    def bar_custom(current, total, width=80):
        print("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))


    try:
        print('Iniciando o download do arquivo ' + nomeMaterial)
        url = str(opec.GetEnderecos('1',str(material['idMaterial']))['enderecos'][0])
    except:
        print('Falha em obter o endereco do arquivo ' + nomeMaterial)

    try:
        print('Baixando ' + nomeMaterial)
        print(url)
        wget.download(url, path + nomeMaterial)

        #Insere na lista de donwloads ok
        arquivo_donwload = open(path + 'listadownload_ok.txt','a+')
        arquivo_donwload.write(str(material['codMaterial'])+ '\n')
        arquivo_donwload.close()

        #TODO:ATUALIZAR UMA LISTA DE ARQUIVOS JA BAIXADOS E OK
    except:
        print('Falha ao fazer donwload do arquivo ' + nomeMaterial)

        #Insere na lista de arquivos com problema no download
        arquivo_donwload = open(path + 'listadownload_bad.txt','a+')
        arquivo_donwload.write(str(material['codMaterial'])+ '\n')
        arquivo_donwload.close()

        #TODO: TRANSFERIR PARA UMA LISTA/ARQUIVO COM OS MATERIAIS COM PROBLEMAS

    try:
        arquivo = open(path + nomeMaterial, 'rb').read()
        md5_arquivo = hashlib.md5(arquivo)
        md5_final = md5_arquivo.hexdigest()
    except:
        print('Não foi possivel chevar a intergridade do arquivo ' + nomeMaterial)
        md5_final = ''

    if md5_original == md5_final:
        print('ARQUIVO INTEGRO')
        print(md5_final)
    else:
        print('ARQUIVO COM PROBLEMA')

    print()


