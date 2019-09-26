import api_globo_poo
import wget
import hashlib
import dateutil.relativedelta
import datetime
import requests
import time
from SMWinservice import SMWinservice

#_______________________________________________________________________

def baixar_arquivo_alternativo(url, endereco):
    resposta = requests.get(url, stream=True, verify=False) #AQUI
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
                for parte in resposta.iter_content(chunk_size=256): #AQUI TBM
                    novo_arquivo.write(parte)
        #print("Download finalizado. Arquivo salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()

path = 'D:\\ftp\\SISCOM\\' # destino dos aquivos de comerciais
path_api = 'D:\\ftp\\SISCOM\\' # destino dos aquivos de .py fonte

#_______________________________________________________________________


class PythonCornerExample(SMWinservice):
    _svc_name_ = "Download_api_globo"
    _svc_display_name_ = "Servido de download da api da globo"
    _svc_description_ = "Este servico baixa automaticamente os arquivos da lista de comerciais da API da GLOBO"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        i = 0
        while self.isrunning:
            # _______________________________________________________________________
            #
            #
            #   BLOCO DE PROGRAMA EM LOOP
            #
            # _______________________________________________________________________
            contador_tentativas = 0
            while contador_tentativas <= 3:

                contador_tentativas = 1

                opec = api_globo_poo.apiGlobo()

                lista_ok = []
                # Atualizando a lista_ok baseado no arquivo listadownload_ok.txt
                try:
                    arq_lista_ok = open(path_api + 'listadownload_ok.txt', 'r')
                    for linha in arq_lista_ok:
                        lista_ok.append(int(linha.replace('\n', '')))
                    # print("LISTA DE MATERIAL JA BAIXADO E OK!")
                    # print(lista_ok)
                    arq_lista_ok.close()
                except:
                    lista_nao_ok = []

                # Atualizando a lista_nao_ok baseado no arquivo listadownload_bad.txt
                try:
                    arq_lista_nao_ok = open(path_api + 'listadownload_bad.txt', 'r')
                    for linha in arq_lista_nao_ok:
                        lista_nao_ok.append(int(linha.replace('\n', '')))
                    # print('LISTA DE MATERIAL BAD!')
                    # print(lista_nao_ok)
                    arq_lista_nao_ok.close()
                    # limpando o arquivo listadownload_bad.txt para atualizacao dentro do bloco de checagem de download
                    arq_lista_nao_ok = open(path_api + 'listadownload_bad.txt', 'w')
                    arq_lista_nao_ok.close()
                except:
                    # print("Problema ao ler o arquivo de download bad!")
                    # TODO: apagar o arquivo para nova lista ser gerada
                    data_de = datetime.datetime.strptime(str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day), "%Y-%m-%d")
                    novo_data_de = data_de - dateutil.relativedelta.relativedelta(days=60)
                    data = str(novo_data_de.year) + "-" + str(novo_data_de.month) + "-" + str(novo_data_de.day)

                    # TODO:VERIFICAR MATERIAL DA CASA VATICANO, O QUE FALTA PARA COMPLETAR O ENDERECO, POIS NÃO FAZ DOWNLOAD

                # obtendo lista atualizada do siscom
                lista_material_opec = opec.GetMateriais(dataDe=[data], cdMateriais=[])

                # listando e comparando com lista existente

                lista_nova_tentativa = []
                # print('contudo da lista nova tentativa')
                # print(lista_nova_tentativa)
                for material in lista_material_opec:

                    if material['codMaterial'] in lista_ok:
                        pass
                    else:
                        # adicionar na lista de nova tentativa de download
                        lista_nova_tentativa.append(material['codMaterial'])
                        # print(str(material['codMaterial']) + " CODIGO DE MATERIAL NAO EXISTE - NOVA TENTATIVA ")

                lista_material_opec = opec.GetMateriais(dataDe=[data], cdMateriais=[lista_nova_tentativa])

                if not lista_nova_tentativa:
                    lista_material_opec.clear()  # Limpando a lista de download quando nao nescessita de tentativas

                for material in lista_material_opec:
                    # print(material)
                    nomeMaterial = material['nomeArquivo'].replace(' ',
                                                                   '_')  # retira os espacos do nome do arquivo, substitui por underline
                    md5_original = material['md5']

                    try:
                        # print('Iniciando o download do arquivo ' + nomeMaterial)
                        url = str(opec.GetEnderecos('1', str(material['idMaterial']))['enderecos'][0])
                    except:
                        pass

                    if material['player'] == 'VATI':  # Caso de servidor com requisicao de certificado
                        try:

                            # Iniciar download alternativo
                            # print('Baixando ' + nomeMaterial)
                            # print(url)
                            baixar_arquivo_alternativo(url, path + nomeMaterial)
                            # Insere na lista de donwloads ok
                            arquivo_donwload = open(path_api + 'listadownload_ok.txt', 'a+')
                            arquivo_donwload.write(str(material['codMaterial']) + '\n')
                            arquivo_donwload.close()


                        except:

                            # print('Falha ao fazer donwload do arquivo ' + nomeMaterial)
                            # Insere na lista de arquivos com problema no download
                            arquivo_donwload = open(path_api + 'listadownload_bad.txt', 'a+')
                            arquivo_donwload.write(str(material['codMaterial']) + '\n')
                            arquivo_donwload.close()

                    else:
                        # Bloco de download padrao
                        try:
                            # print('Baixando ' + nomeMaterial)
                            # print(url)
                            wget.download(url, path + nomeMaterial)

                            # Insere na lista de donwloads ok
                            arquivo_donwload = open(path_api + 'listadownload_ok.txt', 'a+')
                            arquivo_donwload.write(str(material['codMaterial']) + '\n')
                            arquivo_donwload.close()

                        except:
                            # print('Falha ao fazer donwload do arquivo ' + nomeMaterial)
                            # Insere na lista de arquivos com problema no download
                            arquivo_donwload = open(path_api + 'listadownload_bad.txt', 'a+')
                            arquivo_donwload.write(str(material['codMaterial']) + '\n')
                            arquivo_donwload.close()

                    try:
                        arquivo = open(path + nomeMaterial, 'rb').read()
                        md5_arquivo = hashlib.md5(arquivo)
                        md5_final = md5_arquivo.hexdigest()
                    except:
                        # print('Não foi possivel chevar a intergridade do arquivo ' + nomeMaterial)
                        md5_final = ''

                    if md5_original == md5_final:
                        pass
                    else:
                        pass

                time.sleep(120)  # tempo de espera para a proxima consulta


#_______________________________________________________________________
if __name__ == '__main__':
    download_api_globo.parse_command_line()

# pip install pywin32

#python ...pywin32_postinstall.py -install