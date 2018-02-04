import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura
    a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))
    
    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    
    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da
    sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def separa_caracter(palavra):
    '''A funcao recebe uma palavra e devolve uma lista das letras dentro da palavra'''
    return palavra.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que
    aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    
    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras
    diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    
    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau
    de similaridade nas assinaturas.'''
    sab = 0
    for i in range(6):
        sab += abs(as_a[i] - as_b[i])
    return round(sab/6, 2)


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do
    texto.'''
    lista_assinaturas = []
    sentencas = separa_sentencas(texto)
    quant_sentencas = []
    quant_frases_p_sentenca = []
    quant_palavras_p_frase = []
    total_palavras = []
    total_frases = []
    total_sentencas = []
    total_caracter = []
    unicas_total = 0
    diferentes_total = 0
    for elemento_lista in sentencas:
        total_sentencas.append(elemento_lista)
    quant_sentencas.append(len(sentencas))  # armazena na lista a quantidade de sentencas de um texto
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for elemento_lista in frases:
            total_frases.append(elemento_lista)
        quant_frases_p_sentenca.append(len(frases))
        for frase in frases:
            palavras = separa_palavras(frase)
            for elemento_lista in palavras:
                total_palavras.append(elemento_lista)  # lista com todas as palavras
            quant_palavras_p_frase.append(len(palavras))
            unicas_total = n_palavras_unicas(total_palavras)
            diferentes_total = n_palavras_diferentes(total_palavras)
    for elementos in total_palavras:
        for caracter in elementos:
            total_caracter.append(caracter)
    quantidade_total_caracter = len(total_caracter)
    quantidade_total_palavras = len(total_palavras)
    quantidade_total_frases = sum(quant_frases_p_sentenca)
    quantidade_total_sentencas = sum(quant_sentencas)
    # calculos:
    # Tamanho médio de palavra: Média simples do número de caracteres por palavra.
    wal = round((quantidade_total_caracter / quantidade_total_palavras), 2)
    # Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
    ttr = round((diferentes_total / quantidade_total_palavras), 2)
    # Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras. Por exemplo, na frase "O gato caçava o	rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 3 que aparecem só uma vez (gato, caçava, rato). Nessa frase, a relação	Hapax Legomana vale 35=0.6
    hlr = round((unicas_total / quantidade_total_palavras), 2)
    # Complexidade de sentença é o número total de frases divido pelo número de sentenças.
    sac = round((quantidade_total_frases / quantidade_total_sentencas), 2)
    # Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças (os caracteres que separam	uma sentença da outra não devem ser contabilizados como parte da sentença).
    sal = round((quantidade_total_caracter / quantidade_total_sentencas), 2)
    # Tamanho médio de frase: Média simples do número de caracteres por frase. -> calculo do numero total de caracteres dividido por numero total de frases
    pal = round((quantidade_total_caracter / quantidade_total_frases), 2)
    assinaturas = [wal, ttr, hlr, sal, sac, pal]
    lista_assinaturas.append(assinaturas)
    return lista_assinaturas


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o
    numero (1 a n) do texto com maior probabilidade de ter sido infectado
    por COH-PIAH.'''
    lista_assinaturas = []
    grau_similaridade = []
    for texto in textos:
        lista_assinaturas.append(calcula_assinatura(texto))
    for [assinatura] in lista_assinaturas:
        grau_similaridade.append(compara_assinatura(ass_cp,assinatura))
    return grau_similaridade.index(min(grau_similaridade)) + 1



def main():
    # textos = le_textos()# faz a leitura dos textos e armazena em textos
    textos = ['Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso".Quero para mim o espírito [d]esta frase,transformada a forma para a casar como eu sou:Viver não é necessário; o que é necessário é criar.Não conto gozar a minha vida; nem em gozá-la penso.Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo.Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha.Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.', 'Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.', 'NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.']
    #textos = ['a 1, oi teu bem. ola','b 2, teste .paranaue','c 3, teste1 .gingolo']
    #textos = ['O gato cacava o rato','O gato cacava o rato','O gato cacava o rato']
    #textos = ['ola, este eh um teste. Bom dia hoje vamos ter linhas de programacao sendo digitadas, e quando isso acontence temos diversao.','Hoje o dia amanheceu assim, como assim, se eh mesmo assim. A vida nos leva a cada coisa estranha, parece que o mundo da voltas e mais voltas']
    
    assinatura_teste = [4.79,0.72,0.56,80.5,2.5,31.6]
    print('***************************************')
    #assinatura_teste = le_assinatura()
    #textos = le_textos()
    print('\nO autor do texto {} está infectado com COH-PIAH'.format(avalia_textos(textos,assinatura_teste)))
    
    
main()

'''
O resultado dos testes com seu programa foi:
***** [0.25 pontos]: Testando calculo assinatura (text = NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.) - Falhou
***** TypeError: unsupported operand type(s) for -: 'list' and 'float'
***** [0.25 pontos]: Testando calculo assinatura (text = Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.) - Falhou
***** TypeError: unsupported operand type(s) for -: 'list' and 'float'
***** [0.25 pontos]: Testando calculo assinatura (text = Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso".Quero para mim o espírito [d]esta frase,transformada a forma para a casar como eu sou:Viver não é necessário; o que é necessário é criar.Não conto gozar a minha vida; nem em gozá-la penso.Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo.Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha.Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.) - Falhou
***** TypeError: unsupported operand type(s) for -: 'list' and 'float'
***** [0.5 pontos]: Testando avaliação dos textos (Textos = ['Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso".Quero para mim o espírito [d]esta frase,transformada a forma para a casar como eu sou:Viver não é necessário; o que é necessário é criar.Não conto gozar a minha vida; nem em gozá-la penso.Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo.Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha.Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.', 'Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.', 'NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.'] , Assinatura = [4.79, 0.72, 0.56, 80.5, 2.5, 31.6] ) - Falhou
***** AssertionError: Esperado: 2; recebido: 1
'''
