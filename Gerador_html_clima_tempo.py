from CLIMA_TEMPO_OK import lista_ids_cidades,extrai_campos_importantes_arquivo

with open('climatempo_monitor.html', "w") as pagina:
    pagina.write('''
            <!doctype html>
            <html>
                <head>
                    <meta charset="UTF-8">
                    <title>Clima tempo BDR, JT1 e JT2</title>
                    <style>
                        html, body, h1, h2, h3, h4, p {
                            margin:0;
                            padding:0;
                        }
            
                        html {
                            background:rgb(229,229,229);
                        }
            
                        article, aside, section, header, footer, nav {
                            display:block;
                        }
            
                        main {
                            width:1580px;
                            background-color:rgb(255,255,255);
                            font-family:Arial, Helvetica, sans-serif;
                            font-size:14px;
                            box-shadow: 0 0 10px #666;
                            margin:10px auto;
                            padding:10px;
                        }
            
                        header {
                            padding:25px;
                            background-color:rgb(255,102,51);
                            text-align:center;
                            margin-bottom:20px;
                        }
            
                        header h1 {
                            font-size:1.3em;
                            color:rgb(255,255,255);
                        }
                        img {
                            align-content:stretch;
                        }
                        
                        section {
                            background-color:rgb(153,204,51);
                            align-content: center;
                            height:160px;
                            width:180px;
                            margin: 1px;
                            text-align:left;
                            color:rgb(0,0,0);
                            
                            padding: 5px;
                        }
            
                        .janela1 {
                            float: left;
                           
                        }
            
                        .janela2 {
                            float: left;
                           
                            
                        }
                        .janela3 {
                            float: left;
                            
                            
                        }
                        .janela4 {
                            float: left;
                            
                            
                        }
                        .janela5 {
                            float: left;
                            
                            
                        }
                        .janela6 {
                           
                            float: left;
                            
                        }
                        .janela7 {
                            
                            float: left;
                            
                        }
                        .janela8 {
                           
                            float: left;
                            
                        }
                        .janela9 {
                            
                            float: left;
                            
                        }
                        .janela10 {
                            
                            float: left;
                            
                        }
                        .janela11 {
                            
                            float: left;
                            
                        }
                        .janela12 {
                            
                            float: left;
                            
                        }
                        .janela13 {
                            
                            float: left;
                            
                        }
                        .janela14 {
                            
                            float: left;
                            
                        }
                        .janela15 {
                            
                            float: left;
                            
                        }
                        .janela16 {
                            
                            float: left;
                            
                        }
                        .janela17 {
                            
                            float: left;
                            
                        }
                        .janela18 {
                           
                            float: left;
                            
                        }
                        .janela19 {
                          
                            float: left;
                            
                        }
                        .janela20 {
                            
                            float: left;
                            
                        }
                        .janela21 {
                            
                            float: left;
                            
                        }
                        .janela22 {
                           
                            float: left;
                            
                        }
                        .janela23 {
                            
                            float: left;
                            
                        }
                        .janela24 {
                            
                            float: left;
                            
                        }
                        .janela25 {
                            
                            float: left;
                            
                        }
                        .janela26 {
                            
                            float: left;
                            
                        }
                        .janela27 {
                            
                            float: left;
                            
                        }
                        .janela28 {
                            
                            float: left;
                            
                        }
                        .janela29 {
                            
                            float: left;
                            
                        }
                        .janela30 {
                           
                            float: left;
                            
                        }
            
            
                        footer {
                            padding:5px;
                            background-color:rgb(204,153,51);
                            text-align:center;
                            color:rgb(255,255,255);
                            clear: both;
                            margin-top:20px;
                            
                        }
                    </style>
                </head>
            
                <body>
                    <main>
                        <header>
                            <h1>MONITORAMENTO DE TEMPERATURA DAS CIDADES - COBERTURA TV TRIBUNA</h1>
                        </header>
            ''')
pagina.close()
with open('climatempo_monitor.html', "a") as pagina:
    numeroJanela = 0
    for id_cidade in lista_ids_cidades:
        numeroJanela += 1
        pagina.write('''<section class="janela{0}">\n'''.format(numeroJanela))
        pagina.write('<p>{0}</p>\n'.format(str(extrai_campos_importantes_arquivo(id_cidade)[0]).upper()))
        pagina.write('''<p>Temperatura {0}</p>\n'''.format(extrai_campos_importantes_arquivo(id_cidade)[1]))
        pagina.write('''<p><img src="C:\\Users\\dkscr\\Downloads\\realistic\\realistic\\128px\\{0}.png"></p>\n'''.format(extrai_campos_importantes_arquivo(id_cidade)[2]))
        pagina.write("</section>\n")

pagina.close()

with open('climatempo_monitor.html', "a") as pagina:
    pagina.write('''            
                
                <section class="janela30">
                </section>
                <footer>GRUPO TRIBUNA + CLIMATEMPO</footer>
            </main>
        </body>
    </html>
        
        
    ''')
pagina.close()

