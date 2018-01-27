def computador_escolhe_jogada(n, m):
    resto = n % (m + 1)
    if (resto < m):
        return resto
    else:
        return m
    
def usuario_escolhe_jogada(n, m):
    jogada = int(input('Quantas pecas voce vai tirar? '))
    escolhe = True
    while escolhe:
        if (jogada <= m and jogada > 0):
            escolhe = False
            return jogada
        else:
            print('Oops! Jogada invalida! Tente de novo. \n')
            jogada = int(input('Quantas pecas voce vai tirar? '))
#TODO CHECAR O CODIGO E TESTAR
def campeonato():
    numero_partidas = 1
    usuario = 0
    computador = 0
    while numero_partidas != 4:
        print('*** Rodada {} ***\n'.format(numero_partidas))
        ganhador = partida()
        if ganhador:
            usuario += 1
        else:
            computador += 1


        numero_partidas += 1
    
    print('*** Final do campeonato ***')
    print('Placar: Você {} x {} Computador'.format(usuario, computador))
    
def main():
    print('Bem-vindo ao jogo do NIM! \nEscolha: ')
    print('1 - para jogar uma partida isolada')
    print('2 - para jogar um campeonato ')
    partidas = int(input())
    if partidas == 1:  # inicializa partida individual
        partida()
    elif partidas == 2:  # inicializa campeonato
        campeonato()
    else:
        print('entrada invalida !!!')
    

def partida():
    n = int(input('Quantas pecas? '))
    m = int(input('Limite de pecas por jogada? '))
    jogada = True
    if n % (m+1) == 0:# define quem inicia a partida
        print('\nVoce comeca!')
        jogada_usuario = usuario_escolhe_jogada(n, m)
        n -= jogada_usuario
        print('Voce tirou {} peca'.format(jogada_usuario))
        print('Agora resta no tabuleiro {} peca(s)\n'.format(n))
        jogada = False
    else:
        print('\nComputador comeca!')
        jogada_computador = computador_escolhe_jogada(n, m)
        n -= jogada_computador
        print('O computador tirou {} peca'.format(jogada_computador))
        print('Agora resta no tabuleiro {} peca(s)\n'.format(n))
    
    while n != 0:
        if jogada:
            jogada_usuario = usuario_escolhe_jogada(n, m)
            n -= jogada_usuario
            print('Voce tirou {} peca'.format(jogada_usuario))
            print('Agora resta no tabuleiro {} peca(s)\n'.format(n))
            jogada = not jogada
        
        else:
            jogada_computador = computador_escolhe_jogada(n, m)
            n -= jogada_computador
            print('O computador tirou {} peca'.format(jogada_computador))
            print('Agora resta no tabuleiro {} peca(s)\n'.format(n))
            jogada = not jogada
    
    if not jogada:
        print('Fim de jogo! Voce ganhou!')
        return True
    else:
        print('Fim de jogo! O Computador ganhou!')
        return False
      
def test():
  print('ola')
  
      
main()
