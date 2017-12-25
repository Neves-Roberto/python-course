#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
#e calcule e mostre o comprimento da hipotenusa.
#cateto oposto
#cateto adjacente
#hipotenusa
import math
ca = float(input('Digite o cateto adjacente: '))
co = float(input('Digite o cateto oposto: '))
hi = math.sqrt(pow(ca,2)+pow(co,2))
print('a hipotenusa do triangulo retangulo é {:.2f}'.format(hi))

