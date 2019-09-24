from tkinter import *
from datetime import datetime
import api_globo
hoje = datetime.now()
hoje_formatado = str(hoje.year) + '-' + str(hoje.month) + '-' + str(hoje.day)

class Application:
    def __init__(self, master=None):

        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer["pady"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer["pady"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()


        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer["padx"] = 20
        self.sextoContainer["pady"] = 20
        self.sextoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="CONSULTA OPEC - SISCOM API GLOBO")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.cdMaterialLabel = Label(self.segundoContainer, text="CÓDIGO DE MATERIAL:", font=self.fontePadrao)
        self.cdMaterialLabel.pack(side=LEFT)

        self.cdMaterialInput = Entry(self.segundoContainer)
        self.cdMaterialInput["width"] = 30
        self.cdMaterialInput["font"] = self.fontePadrao
        self.cdMaterialInput.pack(side=LEFT)

        self.dataDeLabel = Label(self.terceiroContainer, text="DATA DE: [AAAA-MM-DD]:", font=self.fontePadrao)
        self.dataDeLabel.pack(side=LEFT)

        self.dataAteLabel = Label(self.quartoContainer, text="DATA ATE: [AAAA-MM-DD]:", font=self.fontePadrao)
        self.dataAteLabel.pack(side=LEFT)

        self.dataDe = Entry(self.terceiroContainer)
        self.dataDe["width"] = 30
        self.dataDe["font"] = self.fontePadrao
        self.dataDe.insert(END,hoje_formatado)
        self.dataDe.pack(side=LEFT)

        self.dataAte = Entry(self.quartoContainer)
        self.dataAte["width"] = 30
        self.dataAte["font"] = self.fontePadrao
        self.dataAte.insert(END, hoje_formatado)
        self.dataAte.pack(side=LEFT)

        self.Pesquisar = Button(self.quintoContainer)
        self.Pesquisar["text"] = "PESQUISAR MATERIAL"
        self.Pesquisar["font"] = ("Calibri", "12","bold")
        self.Pesquisar["width"] = 20
        self.Pesquisar["command"] = self.verificaSenha
        self.Pesquisar.pack()

        self.mensagem = Label(self.quintoContainer, text="Obs: Pesquisas sem código de mateiral retorna todos os materiais do filtro DATA", font=self.fontePadrao)
        self.mensagem.pack()


        self.status = Label(self.sextoContainer,text="",font=self.fontePadrao)
        #self.status["text"] = str(api_globo.status_api)
        self.status.pack()

    # Método verificar senha
    def verificaSenha(self):

        codigoMaterialIn = self.cdMaterialInput.get()
        dataDe = self.dataDe.get()
        dataAte = self.dataAte.get()
        #senha = self.senha.get()
        print("gui")
        print(dataDe)
        print(dataAte)
        print(codigoMaterialIn)
        print("api")

        api_globo.GerarListaMateriais(dataDe,dataAte,str(codigoMaterialIn).split(','))



root = Tk()
root.title("OPEC TRIBUNA - CONSULTA API GLOBO V 0.1 BETA")
#root.iconbitmap(r'api_globo.ico')
Application(root)
root.mainloop()