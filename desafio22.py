#crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiusculas
#o nome com todas as letras minusculas
#quantas letras ao todo (sem considerar os espaços)
#quantas letras tem o primeiro nome

nome = str(input('Digite o nome completo : '))
#nome = 'Flavio nunes dos santos'
print('nome em maiusculas {}'.format(nome.upper()))
print('nome em minusculas {}'.format(nome.lower()))
quantidade = len(nome)
espacos = nome.count(' ')
print('quantidade total {}, quantidade de espaços {}, quantidade sem espaços {}'.format(quantidade, espacos, (quantidade-espacos)))
split_nome = nome.split()
print('quantidade de letras primeiro nome: {}'.format(len(split_nome[0])))