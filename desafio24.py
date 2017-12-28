#crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome 'SANTO'
#cidade = 'Santo antonio do parnaiba'
cidade = input('Digite o nome de uma cidade: ')
cidade_split = cidade.lower().split()
print(cidade_split)
print('Tem santo? {}'.format('santo' in cidade_split[0]))
