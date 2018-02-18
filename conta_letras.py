'''
Exercício 1: Contando vogais ou consoantes

Escreva a função conta_letras(frase, contar="vogais"), que recebe como primeiro parâmetro uma string
contendo uma frase e como segundo parâmetro uma outra string. Este segundo parâmetro deve ser opcional.

Quando o segundo parâmetro for definido como "vogais", a função deve devolver o numero de vogais
presentes na frase. Quando ele for definido como "consoantes", a função deve devolver o número de
consoantes presentes na frase. Se este parâmetro não for passado para a função, deve-se assumir o
valor "vogais" para o parâmetro.

Exemplos:
conta_letras('programamos em python')
# deve devolver 6

conta_letras('programamos em python', 'vogais')
# deve devolver 6

conta_letras('programamos em python', 'consoantes')
# deve devolver 13
'''
def conta_letras(frase, contar = 'vogais'):
    cont = 0
    frase = frase.lower()
    lista_vogais = ['a', 'e', 'i', 'o', 'u']
    lista_consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'z']
    for caracter in frase:
        if contar == 'vogais':
            if caracter in lista_vogais:
                cont += 1
        elif contar == 'consoantes':
            if caracter in lista_consoantes:
                cont += 1
    return cont

def test_01():
    assert conta_letras('programamos em python') == 6

def test_02():
    assert conta_letras('programamos em python', 'vogais') == 6
    
def test_03():
    assert conta_letras('programamos em python', 'consoantes') == 13