#Faça um programa que leia um angulo qualquer e mosttre na tela o valor do seno, cosseno e tangente
#desse angulo
import math
anglo = float(input('Digite o angulo em graus: '))*math.pi/180
print('seno {:.2f} cosseno {:.2f} tangente {:.2f}'.format(math.sin(anglo),math.cos(anglo),math.tan(anglo)))