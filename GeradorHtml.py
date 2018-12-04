# TODO Gerar paginas html com conteudo passado da lista
def GerarPaginaEstrutura():
    # TODO montar função de gera arquivo html contendo conteudo da pagina equivalente da consulta realizada
    itens = (
    'idMaterial', 'ptoVenda', 'codMaterial', 'player', 'dataEnvio', 'titulo', 'statusDownload', 'nomeArquivo', 'md5')

    with open('teste.html', "w") as pagina:
        pagina.write('''<!DOCTYPE html>
        <html>
        <head>
        <style>
        table, td, th, tfoot {border:solid 1px #000; padding:5px;}
        th {background-color:#999;}
        caption {font-size:x-large;}
        colgroup {background:#F60;}
        .coluna1 {background:#F66;}
        .coluna2  {background:#F33;}
        .coluna3  {background:#F99;}
        </style>
            </head>
                <body>
                <h1> The HTML style tag </h1>
                <table>
                <colgroup span=3></colgroup>
                <tr>
                ''')
        print('''<!DOCTYPE html>
        <html>
        <head>
        <style>
        table, td, th, tfoot {border:solid 1px #000; padding:5px;}
        th {background-color:#999;}
        caption {font-size:x-large;}
        colgroup {background:#F60;}
        .coluna1 {background:#F66;}
        .coluna2  {background:#F33;}
        .coluna3  {background:#F99;}
        </style>
            </head>
                <body>
                <h1> LISTA MATERIAIS OPEC - API GLOBO </h1>
                <table>
                <colgroup span=3></colgroup>
                <tr>
                ''')
        for item in itens:
            pagina.write("            <th>{0}</th>".format(item))
            print("            <th>{0}</th>".format(item))

        pagina.write('''   </tr>
        <tr>''')
        print('''   </tr>''')


def GerarPaginaCorpo(iten, AtivarLinha, DesativaLinha):
    with open('teste.html', "a") as pagina:
        if AtivarLinha:
            # inserindo linha
            pagina.write("<tr>")
            print("<tr>")

        # inserindo dados
        pagina.write("            <td>{0}</td>".format(iten))
        print("            <td>{0}</td>".format(iten))

        if DesativaLinha:
            # fechando a linha
            pagina.write('''
                    </tr>''')
            print('''</tr>''')
            pagina.close()


def GerarPaginaFim():
    with open('teste.html', "a") as pagina:
        pagina.write('''
                  </table>
                  </body>
                </html> ''')
        print('''

                        </table>
                        </body>
                        </html> ''')
        pagina.close()


GerarPaginaEstrutura()