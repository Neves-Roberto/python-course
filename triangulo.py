class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        # condição para equilátero (todos iguais)
        if self.a == self.b and self.b == self.c:
            return 'equilátero'
        # condição para isósceles (dois lados iguais)
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return 'isósceles'
        # condição para escaleno (todos diferentes)
        else:
            return 'escaleno'


    def retangulo(self):
        from math import sqrt
        triangulo = [self.a, self.b, self.c]
        triangulo = sorted(triangulo)

        ca = triangulo[0]
        co = triangulo[1]
        hipotenusa = sqrt(ca ** 2 + co ** 2)
        if hipotenusa == triangulo[2]:
            return True
        else:
            return False

    def semelhantes(self, triangulo):
        # criando lista com os valores do triangulo 1
        triangulo_1 = [self.a, self.b, self.c]
        triangulo_1 = sorted(triangulo_1)
        # criando lista com os valores do triangulo 2
        triangulo_2 = [triangulo.a, triangulo.b, triangulo.c]
        triangulo_2 = sorted(triangulo_2)
        soma_triangulo_1 = sum(triangulo_1)
        soma_triangulo_2 = sum(triangulo_2)
        if (soma_triangulo_2 >= soma_triangulo_1) and (soma_triangulo_2 % soma_triangulo_1 == 0):
            return True
        elif (soma_triangulo_1 >= soma_triangulo_2) and (soma_triangulo_1 % soma_triangulo_2 == 0):
            return True
        else:
            return False
        
            
