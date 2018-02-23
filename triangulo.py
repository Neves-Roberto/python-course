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
        triangulo = triangulo.sort
        
        ca, co = triangulo[0], triangulo[1]
        hipotenusa = sqrt(ca ** 2 + co ** 2)
        if hipotenusa == triangulo[2]:
            return True
        else:
            return False
