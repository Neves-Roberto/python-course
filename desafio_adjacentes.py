# checa se numero tem adjacente igual

numero = int(input('Digite um numero: '))

temAdjacente = False

if numero != 0:
    while numero // 10 != 0:
        atual = numero % 10
        anterior = (numero // 10) % 10
        numero = numero // 10
        if atual == anterior:
            temAdjacente = True
    
        print('{} {}'.format(atual, anterior))
        
else:
    temAdjacente = False

if temAdjacente:
    print('Tem adjacentes iguais')
else:
    print('Não tem adjacentes iguais')

