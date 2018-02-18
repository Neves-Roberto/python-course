'''
Exercício 2: Ordem lexicográfica

Como pedido no segundo vídeo da semana, escreva a função primeiro_lex(lista) que recebe uma
lista de strings como parâmetro e devolve o primeiro string na ordem lexicográfica. Neste exercício,
considere letras maiúsculas e minúsculas.

Dica: revise a segunda vídeo-aula desta semana.

Exemplos:
primeiro_lex(['oĺá', 'A', 'a', 'casa'])
# deve devolver 'A'

primeiro_lex(['AAAAAA', 'b'])
# deve devolver 'AAAAAA'
'''
def primeiro_lex(lista):
    ultimo_valor_valido = ord('z')
    for palavra in lista:
        valor_caracter = ord(palavra[0])
        if valor_caracter < ultimo_valor_valido:
            string_saida = palavra
            ultimo_valor_valido = valor_caracter
    return string_saida
        
    

def test_01():
    assert primeiro_lex(['oĺá', 'A', 'a', 'casa']) == 'A'

def test_02():
    assert primeiro_lex(['AAAAAA', 'b']) == 'AAAAAA'