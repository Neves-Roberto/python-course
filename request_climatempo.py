import subprocess
import time
dic_cidade_token = {'Santos':'MzY3NQ','São_Vicente':'MzQ4NA','Praia_Grande':'MzU4OQ','Guarujá':'NDIzNA','Cubatão':'NDA0Nw',
                    'Bertioga':'NDM3NA','Itanhaém':'MzgyMw','Iguape':'NDI3Mg','Mongaguá':'MzY5Nw','Peruíbe':'Mzc3MQ',
                    'Barra_do_Chapéu':'NDM2NA','Itaóca':'MzgyNA','Itapirapuã_Paulista':'MzgyOQ','Ribeira':'MzYxOQ',
                    'Iporanga':'MzgxNA','Barra_do_Turvo':'NDM2NQ','Jacupiranga':'Mzg1Mg',
                    'Eldorado':'NDA3OA','Pariquera-Açu':'Mzc1NA','Sete_Barras':'MzQ5Mg','Cajati':'NDQ1MQ',
                    'Juquiá':'Mzg4MA','Miracatu':'Mzk2MA','Cananéia':'NDQ2MA','Ilha_Comprida':'NDI3NA',
                    'Pedro_de_Toledo':'Mzc2Nw','Apiaí':'NDMwMQ','Registro':'MzYwOA'}

r = subprocess.call("C:\\xampp\\apache\\bin\\curl -L --cookie-jar ./somefile -d  \"https://a5.adstream.com/globo/api/materiais/5c3deee9b9fc6663ee38c06e-SPP/download?IDRequisicao=115012019165541&access_token=77cd6210fee0ce1f049d211f5bda7e1d8e75d4d1\"", shell=False)

'''

for cidade in dic_cidade_token.keys():
    r = subprocess.call("C:\\xampp\\apache\\bin\\curl -L --cookie-jar ./somefile -d \"email=jose.menezes@tvtribuna.com&password=TVtribuna.18\" https://tvs.climatempo.com.br/auth", shell=False)
    print('Efetuando Autenticação ...')
    r = subprocess.call("C:\\xampp\\apache\\bin\\curl -L --cookie ./somefile \"https://tvs.climatempo.com.br/download?i={0}==&t=Zm9yZWNhc3QtZml2ZS1kYXlz&u=U1A=\" --output ./{1}.PNG".format(dic_cidade_token[cidade],cidade), shell=False)
    print('Temperaturas da cidade de: '+ str(cidade))
    time.sleep(3)



r = subprocess.call("C:\\xampp\\apache\\bin\\curl -L --cookie-jar ./somefile -d \"email=jose.menezes@tvtribuna.com&password=TVtribuna.18\" https://tvs.climatempo.com.br/auth", shell=False)
print('Efetuando Autenticação ...')
r = subprocess.call("C:\\xampp\\apache\\bin\\curl -L --cookie ./somefile \"https://tvs.climatempo.com.br/download?t=c2F0ZWxsaXRl&r=c3A=\" --output ./satdu.gif", shell=False)
print('Download satdu')
time.sleep(3)

r = subprocess.call("C:\\xampp\\apache\\bin\\curl -L --cookie-jar ./somefile -d \"email=jose.menezes@tvtribuna.com&password=TVtribuna.18\" https://tvs.climatempo.com.br/auth", shell=False)
print('Efetuando Autenticação ...')
r = subprocess.call("C:\\xampp\\apache\\bin\\curl -L --cookie ./somefile \"https://tvs.climatempo.com.br/download?t=c2F0ZWxsaXRl&r=YnI=\" --output ./satbra.gif", shell=False)
print('Download satbra')
time.sleep(3)

r = subprocess.call("C:\\xampp\\apache\\bin\\curl -L --cookie-jar ./somefile -d \"email=jose.menezes@tvtribuna.com&password=TVtribuna.18\" https://tvs.climatempo.com.br/auth", shell=False)
print('Efetuando Autenticação ...')
r = subprocess.call("C:\\xampp\\apache\\bin\\curl -L --cookie ./somefile \"https://tvs.climatempo.com.br/download?t=c2F0ZWxsaXRl&r=c2U=\" --output ./satsudeste.gif", shell=False)
print('Download satsudeste')
time.sleep(3)

r = subprocess.call("C:\\xampp\\apache\\bin\\curl -L --cookie-jar ./somefile -d \"email=jose.menezes@tvtribuna.com&password=TVtribuna.18\" https://tvs.climatempo.com.br/auth", shell=False)
print('Efetuando Autenticação ...')
r = subprocess.call("C:\\xampp\\apache\\bin\\curl -L --cookie ./somefile \"https://tvs.climatempo.com.br/download?t=Zm9yZWNhc3QtbWFwcw==&r=c2U=\" --output ./mapsud.png", shell=False)
print('Download mapsud')



#TODO anexar o conversor de gif para mp4
#TODO adicionar as requisições para os videos e os gifs
 '''