'''
class NomeDaClasse(object):
    atributo1 = None
    
    def metodo(self, args):
        pass
'''

#calculadora.py
class Calculadora(object):


    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

    def subtrai(self):
        return self.a - self.b

    def multiplica(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b
    
c = Calculadora(128, 6)
print(c.a)
print(c.b)
print(c.soma())
print(c.subtrai())
print(c.multiplica())
print(c.divide())


