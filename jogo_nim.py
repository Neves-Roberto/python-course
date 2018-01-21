
def computador_escolhe_jogada(n, m):
    resto = n % (m + 1)
    if (resto < m):
        return resto
    else:
        return m
    
    
def usuario_escolhe_jogada(n, m):
    jogada = int(input('Qantas peças você vai tirar? '))
    escolhe = True
    while escolhe:
        if (jogada <= m and jogada > 0):
            escolhe = False
            return jogada
        else:
            print('Oops! Jogada invalida! Tente de novo. \n')
            jogada = int(input('Qantas peças você vai tirar? '))
    

def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    jogada = True
    if n % (m+1) == 0:# define quem inicia a partida
        print('Voce começa!')
        n -= usuario_escolhe_jogada(n, m)
    else:
        print('Computador começa!')
        print(computador_escolhe_jogada(n, m))
        jogada = False

    while n != 0:
        if jogada:
            n -= usuario_escolhe_jogada(n, m)
            jogada = not jogada
            
        else:

            n -= computador_escolhe_jogada(n, m)
            jogada = not jogada
            
partida()