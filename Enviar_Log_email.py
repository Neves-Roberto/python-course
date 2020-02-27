from email.mime.multipart import MIMEMultipart
import dateutil.relativedelta
import datetime
import smtplib
from email.mime.text import MIMEText

path_api = 'C:\\Users\\projetos\\PycharmProjects\\python-course\\'

DIAS = 1

data_hoje_log = str(datetime.datetime.now().day) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().year)
data_de = datetime.datetime.strptime(str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day), "%Y-%m-%d")
novo_data_de = data_de - dateutil.relativedelta.relativedelta(days=DIAS)
data =  str(novo_data_de.day) + "-" + str(novo_data_de.month) + "-" +str(novo_data_de.year)
print(data)
# conexão com os servidores do google
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
# username ou email para logar no servidor
username = 'dkscript@gmail.com'
password = 'desptro007'

from_addr = 'dkscript@gmail.com'
to_addrs = ['flavio.santos@tvtribuna.com']

message = MIMEMultipart()
message['subject'] = 'Log Download API GLOBO ' + data
message['from'] = from_addr
message['to'] = ', '.join(to_addrs)
#Anexa arquivo de log
try:

    with open(path_api + 'log_download_api_' + data + '.txt', 'r') as arquivo_log:
        logMime = MIMEText(arquivo_log.read(),_subtype='txt')
        logMime.add_header('content-disposition', 'attachment', filename='log_download_api_' + data + '.txt')
    message.attach(logMime)
except:
    message = MIMEText('Problemas para encontrar o arquivo ' + path_api + 'log_download_api_' + data + '.txt')
    message['subject'] = 'Log Download API GLOBO ' + data
    message['from'] = from_addr
    message['to'] = ', '.join(to_addrs)
# conectaremos de forma segura usando SSL
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
# para interagir com um servidor externo precisaremos
# fazer login nele
server.login(username, password)
server.sendmail(from_addr, to_addrs, message.as_string())
server.quit()