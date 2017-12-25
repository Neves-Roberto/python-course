#um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido

import random
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
sorteio = random.randint(1, 4)
print('aluno sorteado numero {}, parabens {}'.format(sorteio, aluno[sorteio]))

#falta o uso de variavel que utilize indice para localizar o objeto desejado