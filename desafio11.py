#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a
#quantidade de tinta nescessaria para pinta-la, sabendo que cada litro de tinta printa uma area
#de 2 metros quadrados

altura = float(input('Digite a altura da parede (m): '))
largura = float(input('Digite a largura da parede (m): '))
area = largura * altura
quantidade_tinta = area / 2
print('A área total da parede é {}, e a quantidade de tinta é {} litros'.format(area, quantidade_tinta))