import api_globo_poo
import wget
import hashlib
import dateutil.relativedelta
import datetime
import requests
import time,os,re
import json
import smtplib
from email.mime.text import MIMEText

# conexão com os servidores do google
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
# username ou email para logar no servidor
username = 'projetos.tvtribuna@gmail.com'
password = 'desptro01'#digitar a senha no servidor

from_addr = 'projetos.tvtribuna@gmail.com'
to_addrs = ['flavio.santos@tvtribuna.com','dkscript@gmail.com']#lista de emails

# a biblioteca email possuí vários templates
# para diferentes formatos de mensagem
# neste caso usaremos MIMEText para enviar
# somente texto
"""message = MIMEText('Hello World')
message['subject'] = 'Hello'
message['from'] = from_addr
message['to'] = ', '.join(to_addrs)"""

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)

"""# conectaremos de forma segura usando SSL
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
# para interagir com um servidor externo precisaremos
# fazer login nele
server.login(username, password)
server.sendmail(from_addr, to_addrs, message.as_string())
server.quit()
"""




def lista_arquivos(diretorio,extensao='mxf'):
    pattern = '^\d+'
    pasta = diretorio# diretorio onde localiza os arquivos .extensao
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    lista_arquivos_extensao = [re.findall(pattern,arq.replace(path,''))[0] for arq in arquivos if arq.lower().endswith(extensao.lower())]  # lista com todos os arquivos .extensao no diretorio
    return lista_arquivos_extensao

def baixar_arquivo_alternativo(url, endereco):
    resposta = requests.get(url, stream=True, verify=False) #AQUI
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
                for parte in resposta.iter_content(chunk_size=256): #AQUI TBM
                    novo_arquivo.write(parte)
        #print("Download finalizado. Arquivo salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()

#path = 'C:\\Users\\projetos\\PycharmProjects\\python-course\\mxf\\'
#path = 'Y:\\SISCOM\\'
path = 'C:\\Users\\dkscr\\PycharmProjects\\python-course\\SISCOM\\'
path_api = 'C:\\Users\\dkscr\\PycharmProjects\\python-course\\'
#path_api = 'C:\\Users\\projetos\\PycharmProjects\\python-course\\Comerciais_Api_globo\\'

try:

    mensagem = 'Iniciado o download_api_globo'
    message = MIMEText(mensagem)
    message['subject'] = 'START DOWNLOAD_API_GLOBO' # assunto
    message['from'] = from_addr
    message['to'] = ', '.join(to_addrs)
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, message.as_string())
    server.quit()
except:
    print('Nao foi possivel enviar o email de inicio')
    arquivo_log = open(path_api + 'log_download_api.txt', 'a+')
    mensagem = 'Nao foi possivel enviar o email de inicio\n'
    arquivo_log.write(mensagem)
    arquivo_log.close()


teste = True

contador_tentativas = 0
while contador_tentativas <= 3:
    data_hoje_log = str(datetime.datetime.now().day)+'-'+str(datetime.datetime.now().month)+'-'+str(datetime.datetime.now().year)
    print(data_hoje_log)

    try:
        config_arq = open('config.json')
        config_json = json.loads(config_arq.readlines()[0])
        config_arq.close
    except FileNotFoundError:
        print("Arquivo de configuração não encontrado!")
        print("Aplicando valores padroes:")
        DIAS = 1
        TDLY = 120
        print("Criando arquivo de configuracao padrao")
        arq_config = open(path_api + 'config.json', 'w')
        arq_config.write("{\"DIAS\": 1, \"TDLY\": 120 }\n")
        arq_config.write("#Arquivo de configuracao do download_api_globo\n")
        arq_config.write("#Parametro DIAS, quantidade de dias que deseja manter atualizado, 0 eh o mesmo dias, 1 eh o dia atual mais 1 (um) ...\n")
        arq_config.write("#Parametro TDLY eh o tempo de delay para a nova verificação em segundos.\n")
        arq_config.close



    else:
        # Atualizando Variaveis
        DIAS = int(config_json['DIAS'])
        TDLY = int(config_json['TDLY'])

    print("Quantidade de dias " + str(DIAS))
    print("Tempo de delay " + str(TDLY))

    contador_tentativas =1

    opec = api_globo_poo.apiGlobo()

    lista_ok = []
    #atualizando lista baseado na pasta
    arq_lista_ok = open(path_api + 'listadownload_ok.txt', 'w')
    arq_lista_ok.close
    arq_lista_ok = open(path_api + 'listadownload_ok.txt', 'a+')
    for lista_diretorio in lista_arquivos(path):
        arq_lista_ok.write(lista_diretorio + '\n')
    arq_lista_ok.close

    #Atualizando a lista_ok baseado no arquivo listadownload_ok.txt
    try:
        arq_lista_ok = open(path_api + 'listadownload_ok.txt', 'r')
        for linha in arq_lista_ok:
            lista_ok.append(int(linha.replace('\n', '')))
        print("LISTA DE MATERIAL JA BAIXADO E OK!")
        print(lista_ok)
        arq_lista_ok.close()
    except:
        print('Problema ao ler o arquivo download ok!')
    lista_nao_ok = []
    # Atualizando a lista_nao_ok baseado no arquivo listadownload_bad.txt
    try:
        arq_lista_nao_ok = open(path_api + 'listadownload_bad.txt', 'r')
        for linha in arq_lista_nao_ok:
            lista_nao_ok.append(int(linha.replace('\n', '')))
        print('LISTA DE MATERIAL BAD!')
        print(lista_nao_ok)
        arq_lista_nao_ok.close()
        #limpando o arquivo listadownload_bad.txt para atualizacao dentro do bloco de checagem de download
        arq_lista_nao_ok = open(path_api + 'listadownload_bad.txt', 'w')
        arq_lista_nao_ok.close()
    except:
        print("Problema ao ler o arquivo de download bad!")
    #TODO: apagar o arquivo para nova lista ser gerada

    data_de = datetime.datetime.strptime(str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day), "%Y-%m-%d")
    novo_data_de = data_de - dateutil.relativedelta.relativedelta(days=DIAS)
    data = str(novo_data_de.year) + "-" + str(novo_data_de.month) + "-" + str(novo_data_de.day)

    #TODO:VERIFICAR MATERIAL DA CASA VATICANO, O QUE FALTA PARA COMPLETAR O ENDERECO, POIS NÃO FAZ DOWNLOAD


    #obtendo lista atualizada do siscom
    lista_material_opec = opec.GetMateriais(dataDe=[data],cdMateriais=[])

    #listando e comparando com lista existente

    lista_nova_tentativa = []
    print('conteudo da lista nova tentativa')
    print(lista_nova_tentativa)
    for material in lista_material_opec:

        if material['codMaterial'] in lista_ok:
            print(str(material['codMaterial']) + " CODIGO DE MATERIAL JA EXISTE ")
        else:
            # adicionar na lista de nova tentativa de download
            lista_nova_tentativa.append(material['codMaterial'])
            print(str(material['codMaterial']) + " CODIGO DE MATERIAL NAO EXISTE - NOVA TENTATIVA ")



    lista_material_opec = opec.GetMateriais(dataDe=[data],cdMateriais=[lista_nova_tentativa])

    if not lista_nova_tentativa:
        lista_material_opec.clear()# Limpando a lista de download quando nao nescessita de tentativas

    for material in lista_material_opec:
        print(material)
        nomeMaterial = material['nomeArquivo'].replace(' ','_') # retira os espacos do nome do arquivo, substitui por underline
        md5_original = material['md5']


        try:
            print('Iniciando o download do arquivo ' + nomeMaterial)
            url = str(opec.GetEnderecos('1',str(material['idMaterial']))['enderecos'][0])
        except:
            print('Falha ao obter o endereco do arquivo ' + nomeMaterial)

        if material['player'] == 'VATI':# Caso de servidor com requisicao de certificado
            try:

                # Iniciar download alternativo
                print('\nDOWNLOAD ALTERNATIVO DO ARQUIVO ' + nomeMaterial)
                print(url)
                baixar_arquivo_alternativo(url,path + nomeMaterial)
                #Insere na lista de donwloads ok
                arquivo_donwload = open(path_api + 'listadownload_ok.txt','a')
                arquivo_donwload.write(str(material['codMaterial'])+ '\n')
                arquivo_donwload.close()

                # inserir dados no log
                arquivo_log = open(path_api + 'log_download_api_'+data_hoje_log+'.txt','a')
                data_log = datetime.datetime.strptime(
                    str(datetime.datetime.now().day) + '-' + str(datetime.datetime.now().month) + '-' + str(
                        datetime.datetime.now().year) + '-' + str(datetime.datetime.now().hour) + '-' + str(
                        datetime.datetime.now().minute) + '-' + str(datetime.datetime.now().second),
                    "%d-%m-%Y-%H-%M-%S")
                arquivo_log.write(str(data_log) + ' CODIGO ' + str(material['codMaterial']) + ' DOWNLOAD ALTERNATIVO DO ARQUIVO ' + nomeMaterial + '\n')
                arquivo_log.close()

            except:

                print('\nFALHA NO DOWNLOAD ALTERNATIVO DO ARQUIVO ' + nomeMaterial)
                #Insere na lista de arquivos com problema no download
                arquivo_donwload = open(path_api + 'listadownload_bad.txt','a+')
                arquivo_donwload.write(str(material['codMaterial'])+ '\n')
                arquivo_donwload.close()
                # inserir dados no log
                arquivo_log = open(path_api + 'log_download_api_'+data_hoje_log+'.txt', 'a+')
                data_log = datetime.datetime.strptime(
                    str(datetime.datetime.now().day) + '-' + str(datetime.datetime.now().month) + '-' + str(
                        datetime.datetime.now().year) + '-' + str(datetime.datetime.now().hour) + '-' + str(
                        datetime.datetime.now().minute) + '-' + str(datetime.datetime.now().second),
                    "%d-%m-%Y-%H-%M-%S")

                arquivo_log.write(str(data_log) + ' CODIGO ' + str(material['codMaterial']) + ' FALHA NO DOWNLOAD ALTERNATIVO DO ARQUIVO ' + nomeMaterial + '\n')
                arquivo_log.close()

        else:
            #Bloco de download padrao
            try:
                print('\nDOWNLOAD DO ARQUIVO ' + nomeMaterial)
                print(url)
                wget.download(url, path + nomeMaterial)

                #Insere na lista de donwloads ok
                arquivo_donwload = open(path_api + 'listadownload_ok.txt','a+')
                arquivo_donwload.write(str(material['codMaterial'])+ '\n')
                arquivo_donwload.close()

                # inserir dados no log
                arquivo_log = open(path_api + 'log_download_api_'+data_hoje_log+'.txt', 'a+')
                data_log = datetime.datetime.strptime(
                    str(datetime.datetime.now().day) + '-' + str(datetime.datetime.now().month) + '-' + str(
                        datetime.datetime.now().year) + '-' + str(datetime.datetime.now().hour) + '-' + str(
                        datetime.datetime.now().minute) + '-' + str(datetime.datetime.now().second),
                    "%d-%m-%Y-%H-%M-%S")

                arquivo_log.write(str(data_log) + ' CODIGO ' + str(material['codMaterial']) + ' DOWNLOAD DO ARQUIVO ' + nomeMaterial + '\n')
                arquivo_log.close()

            except:
                print('\nFALHA NO DOWNLOAD ARQUIVO ' + nomeMaterial)

                #Insere na lista de arquivos com problema no download
                arquivo_donwload = open(path_api + 'listadownload_bad.txt','a+')
                arquivo_donwload.write(str(material['codMaterial'])+ '\n')
                arquivo_donwload.close()

                # inserir dados no log
                arquivo_log = open(path_api + 'log_download_api_'+data_hoje_log+'.txt', 'a+')
                data_log = datetime.datetime.strptime(
                    str(datetime.datetime.now().day) + '-' + str(datetime.datetime.now().month) + '-' + str(
                        datetime.datetime.now().year) + '-' + str(datetime.datetime.now().hour) + '-' + str(
                        datetime.datetime.now().minute) + '-' + str(datetime.datetime.now().second),
                    "%d-%m-%Y-%H-%M-%S")

                arquivo_log.write(str(data_log) + ' CODIGO ' + str(material['codMaterial']) + ' FALHA NO DOWNLOAD ARQUIVO ' + nomeMaterial + '\n')
                arquivo_log.close()


        try:
            arquivo = open(path + nomeMaterial, 'rb').read()
            md5_arquivo = hashlib.md5(arquivo)
            md5_final = md5_arquivo.hexdigest()
        except:
            print('Não foi possivel chevar a intergridade do arquivo ' + nomeMaterial)
            md5_final = ''



        if md5_original == md5_final:
            print('\nARQUIVO INTEGRO')
            print(md5_final)
            # inserir dados no log
            arquivo_log = open(path_api + 'log_download_api_'+data_hoje_log+'.txt', 'a+')
            data_log = datetime.datetime.strptime(
                str(datetime.datetime.now().day) + '-' + str(datetime.datetime.now().month) + '-' + str(
                    datetime.datetime.now().year) + '-' + str(datetime.datetime.now().hour) + '-' + str(
                    datetime.datetime.now().minute) + '-' + str(datetime.datetime.now().second),
                "%d-%m-%Y-%H-%M-%S")
            mensagem = str(data_log) + ' CODIGO ' + str(material['codMaterial']) + ' VERIFICADO MD5 DO ARQUIVO ' + nomeMaterial + ' MD5 ORIGINAL ' + md5_original + ' MD5 VERIFICADO ' + md5_final + '\n'

            arquivo_log.write(mensagem)
            arquivo_log.close()

            try:
                #Inserir dados do email
                msg_str = str(data_log) + '\n CODIGO ' + str(material['codMaterial']) + '\n VERIFICADO MD5 DO ARQUIVO ' + nomeMaterial + '\n MD5 ORIGINAL ' + md5_original + '\n MD5 VERIFICADO ' + md5_final + '\n PLAYER ' + str(material['player']) + '\n'
                msg = 'DOWNLOAD CONCLUIDO\n' + msg_str
                message = MIMEText(msg)
                message['subject'] = 'DOWNLOAD CONCLUIDO ' + nomeMaterial  # assunto
                message['from'] = from_addr
                message['to'] = ', '.join(to_addrs)
                server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
                server.connect(smtp_ssl_host,smtp_ssl_port)
                server.login(username, password)
                server.sendmail(from_addr, to_addrs, message.as_string())
                server.quit()
            except:
                print('Nao foi possivel enviar email de download concluido')
                arquivo_log = open(path_api + 'log_download_api_'+data_hoje_log+'.txt', 'a+')
                mensagem = 'Nao foi possivel enviar email de download concluido\n'
                arquivo_log.write(mensagem)
                arquivo_log.close()
        else:
            print('\nARQUIVO COM PROBLEMA')
            # inserir dados no log
            arquivo_log = open(path_api + 'log_download_api_'+data_hoje_log+'.txt', 'a+')
            data_log = datetime.datetime.strptime(
                str(datetime.datetime.now().day) + '-' + str(datetime.datetime.now().month) + '-' + str(
                    datetime.datetime.now().year) + '-' + str(datetime.datetime.now().hour) + '-' + str(
                    datetime.datetime.now().minute) + '-' + str(datetime.datetime.now().second),
                "%d-%m-%Y-%H-%M-%S")
            mensagem = str(data_log) + ' CODIGO ' + str(material['codMaterial']) + ' DIVERGENCIA MD5 DO ARQUIVO ' + nomeMaterial + ' MD5 ORIGINAL ' + md5_original + ' MD5 VERIFICADO ' + md5_final + '\n'
            arquivo_log.write(mensagem)

            try:



                msg_str = str(data_log) + '\n CODIGO ' + str(material['codMaterial']) + '\n DIVERGENCIA MD5 DO ARQUIVO ' + nomeMaterial + '\n MD5 ORIGINAL ' + md5_original + '\n MD5 VERIFICADO ' + md5_final + '\n PLAYER ' + str(material['player']) + '\n'
                #conteudo da mensagem de email
                message = MIMEText(msg_str)
                message['subject'] = 'DIVERGENCIA DE NO ARQUIVO ' + nomeMaterial#assunto
                message['from'] = from_addr
                message['to'] = ', '.join(to_addrs)
                server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
                server.connect(smtp_ssl_host, smtp_ssl_port)
                server.login(username, password)
                server.sendmail(from_addr, to_addrs, message.as_string())
                server.quit()
            except:
                print('Nao foi possivel enviar email de divergencia de arqvuivos')
                arquivo_log = open(path_api + 'log_download_api_'+data_hoje_log+'.txt', 'a+')
                mensagem = 'Nao foi possivel enviar email de divergencia de arqvuivos\n'
                arquivo_log.write(mensagem)
                arquivo_log.close()

            try:
                os.remove(path + nomeMaterial)
                mensagem = 'DELETANDO O ARQUIVO ' + nomeMaterial + ' ' + str(material['codMaterial']) + '\n'
                arquivo_log.write(mensagem)

                try:

                    # conteudo da mensagem de email
                    msg_str = str(data_log) + '\n CODIGO ' + str(material['codMaterial']) + '\n DELETANDO O ARQUIVO ' + nomeMaterial + '\n PLAYER ' + str(material['player']) + '\n'
                    message = MIMEText(msg_str)
                    message['subject'] = 'DELETANDO O ARQUIVO ' + nomeMaterial  # assunto
                    message['from'] = from_addr
                    message['to'] = ', '.join(to_addrs)
                    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
                    server.connect(smtp_ssl_host, smtp_ssl_port)
                    server.login(username, password)
                    server.sendmail(from_addr, to_addrs, message.as_string())
                    server.quit()
                except:
                    print('Nao foi possivel enviar email de deletar arqvuivos')
                    arquivo_log = open(path_api + 'log_download_api_'+data_hoje_log+'.txt', 'a+')
                    mensagem = 'Nao foi possivel enviar email de deletar arqvuivos\n'
                    arquivo_log.write(mensagem)
                    arquivo_log.close()

            except:
                arquivo_log.write('NAO FOI POSSIVEL DELETAR O ARQUIVO ' + nomeMaterial + ' ' + str(material['codMaterial']) + '\n')

            arquivo_log.close()

    print(TDLY)


    time.sleep(TDLY)#tempo de espera para a proxima verificacao


