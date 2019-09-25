import api_globo_poo
import dateutil.relativedelta
import datetime
import wget
import hashlib
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
#print(opec.GetMateriais(cdMateriais=[]))
lista_ok = []
arq_lista_ok = open('listadownload_ok.txt','r')
for linha in arq_lista_ok:
    lista_ok.append(int(linha.replace('\n','')))
print(lista_ok)

data_de = datetime.datetime.strptime(str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day), "%Y-%m-%d")
novo_data_de = data_de - dateutil.relativedelta.relativedelta(days=1)
data = str(novo_data_de.year) + "-" + str(novo_data_de.month) + "-" + str(novo_data_de.day)

for num, material in enumerate(opec.GetMateriais(dataDe=[data])):

    if material['codMaterial'] in lista_ok:
        print(str(num) + ' ' + str(material['codMaterial']) + " EXISTE " )
    #print(str(num) + ' ' + str(material['codMaterial']))

