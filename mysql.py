import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='flavio')
cursor = cnx.cursor()
query = ("SELECT nomeproduto, precounitario,tempoentrega FROM produtos")
cursor.execute(query)
for (nomeproduto, precounitario, tempoentrega) in cursor:
  print("{}, {} was hired on {:%d %b %Y}".format(
      nomeproduto, precounitario, tempoentrega))
cursor.close()
cnx.close()