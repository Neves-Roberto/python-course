# checa se numero tem adjacente igual
'''
Exercício 2 - Desafio do vídeo "Repetição com while"

Escreva um programa que receba um número inteiro na entrada e
verifique se o número recebido possui ao menos um dígito com um
dígito adjacente igual a ele. Caso exista, imprima "sim";
se não existir, imprima "não".

Exemplos:

Digite um número inteiro: 123

não

Digite um número inteiro: 3556

sim
'''
numero = int(input('Digite um numero: '))

temAdjacente = False

if numero != 0:
    while numero // 10 != 0:
        atual = numero % 10
        anterior = (numero // 10) % 10
        numero = numero // 10
        if atual == anterior:
            temAdjacente = True
    
        
        
else:
    temAdjacente = False

if temAdjacente:
    print('sim')
else:
    print('não')

