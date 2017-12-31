def main():
    carro1 = Carro('brasilia', 1968, 'amarala', 80)
    carro2 = Carro('fusção', 1981, 'preto', 95)
    
    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)
    

class Carro:
    def __init__(self, modelo, ano, cor, velocidade_max): #metodo init para inicializar o objeto
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
        self.velocidade_max = velocidade_max
        
    def imprima(self):
        if self.velocidade == 0:#parado da para ver o ano
            print('{} {} {}'.format(self.modelo, self.cor, self.ano))
        elif self.velocidade < self.velocidade_max:
            print('{} {} indo a {} km/h'.format(self.modelo, self.cor, self.velocidade))
        else:
            print('{} {} indo muito rapido.... '.format(self.modelo, self.cor))
    
    def acelere(self,velocidade):
        self.velocidade = velocidade
        if self.velocidade > self.velocidade_max:
            self.velocidade = self.velocidade_max
        self.imprima()
        
    def pare(self):
        self.velocidade = 0
        self.imprima()
        
main()

