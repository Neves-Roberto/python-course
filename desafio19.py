#um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido

import random
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
#uso de listas
sorteio = random.choice(lista_alunos)

print('aluno sorteado numero {}, parabens '.format(sorteio))
