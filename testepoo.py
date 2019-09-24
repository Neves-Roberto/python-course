#criancao de classes em poo e heranca
import api_globo_poo
import wget
import hashlib

class Avo:

    '''
    Classe mestre para a hierarquia das outras classes
    criar atributos e metodos referente a classe mestre
    '''

    def __init__(self):
        print('iniciado o construtor de Avo')
        self.familia = 'jordao'
        self.cor_olhos = 'azul'

    def getCorOlhos(self):
        print('A cor dos olhos é ' + self.cor_olhos)

    def setCorOlhos(self,novaCorOlhos):
        self.cor_olhos = novaCorOlhos

class Pai(Avo):

    def __init__(self):
        Avo.__init__(self)
        #self.cor_olhos = 'verde'
        print('iniciado o construtor de Pai')


class Filho(Pai):

    def __init__(self):
        Pai.__init__(self)
        #self.cor_olhos = 'azul-esverdeado'
        print('iniciado o construtor de Filho')

def insereListaOk(idMaterial):
    pass

def insereListaNaoOk(idMaterial):
    pass

#path = 'C:\\Users\\projetos\\PycharmProjects\\python-course\\mxf\\'
path = 'Y:\\SISCOM\\siscom_Teste\\'

opec = api_globo_poo.apiGlobo()

for material in opec.GetMateriais(cdMateriais=[]):
    print(material)
    nomeMaterial = material['nomeArquivo'].replace(' ','_') # retira os espacos do nome do arquivo, substitui por underline
    #print(material['codMaterial'])
    md5_original = material['md5']
    #print(str(material['codMaterial']))
    try:
        print('Iniciando o download do arquivo ' + nomeMaterial)
        url = opec.GetEnderecos('1',str(material['idMaterial']))['enderecos'][0]
    except:
        print('Falha em obter o endereco do arquivo ' + nomeMaterial)

    try:
        print('Baixando ' + nomeMaterial)
        filename = wget.download(url, path)
        #TODO:ATUALIZAR UMA LISTA DE ARQUIVOS JA BAIXADOS E OK
    except:
        print('Falha ao fazer donwload do arquivo ' + nomeMaterial)
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



'''
#url = opec.GetEnderecos('1','298429')['enderecos'][0]
#print(url)
#filename = wget.download(url,"198285_TRATAMENTO 3 DIAS 1DE5.mxf")
arquivo = open("198285_TRATAMENTO 3 DIAS 1DE5.mxf",'rb').read()
md5_arquivo = hashlib.md5(arquivo)
md5_final = md5_arquivo.hexdigest()
if md5_original == md5_final:
    print('ARQUIVO INTEGRO')
    print(md5_final)
else:
    print('ARQUIVO COM PROBLEMA')

print()

'''

