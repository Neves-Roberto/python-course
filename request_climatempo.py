import time
import subprocess

dic_cidade_token = {'Barra_do_Chapéu':'NDM2NA','Itaóca':'MzgyNA','Itapirapuã_Paulista':'MzgyOQ','Ribeira':'MzYxOQ','Iporanga':'MzgxNA','Barra_do_Turvo':'NDM2NQ','Jacupiranga':'Mzg1Mg','Eldorado':'NDA3OA==&t=Zm9yZWNhcQtZml2ZS1kYXlz&u=U1A=','Pariquera-Açu':'Mzc1NA','Sete_Barras':'MzQ5Mg','Cajati':'NDQ1MQ','Juquiá':'Mzg4MA','Miracatu':'Mzk2MA','Cananéia':'NDQ2MA','Ilha_Comprida':'NDI3NA','Pedro_de_Toledo':'Mzc2Nw','Apiaí':'NDMwMQ','Iguape':'NDI3Mg','Registro':'MzYwOA','Peruíbe':'Mzc3MQ','Mongaguá':'MzY5Nw','Itanhaém':'MzgyMw','Bertioga':'NDM3NA','Cubatão':'NDA0Nw','Guarujá':'NDIzNA','Praia_Grande':'MzU4OQ','São_Vicente':'MzQ4NA','Santos':'MzY3NQ'}

for cidade in dic_cidade_token.keys():
    r = subprocess.call("C:\\xampp\\apache\\bin\\curl -L --cookie-jar ./somefile -d \"email=jose.menezes@tvtribuna.com&password=TVtribuna.18\" https://tvs.climatempo.com.br/auth", shell=False)
    print('Efetuando Autenticação ...')
    r = subprocess.call("C:\\xampp\\apache\\bin\\curl -L --cookie ./somefile \"https://tvs.climatempo.com.br/download?i={0}==&t=Zm9yZWNhc3QtZml2ZS1kYXlz&u=U1A=\" --output ./{1}.PNG".format(dic_cidade_token[cidade],cidade), shell=False)
    print('Temperaturas da cidade de: '+ str(cidade))
    time.sleep(1)

#TODO anexar o conversor de gif para mp4
#TODO adicionar as requisições para os videos e os gifs
