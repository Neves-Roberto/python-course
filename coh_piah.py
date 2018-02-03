'''
Traços linguísticos

Nesse exercício utilizaremos as seguintes estatísticas para detectar a doença:

    Tamanho médio de palavra: Média simples do número de caracteres por palavra.
	
    Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
	
    Razão Hapax Legomana: Número de palavras utilizadas uma vez dividido pelo número total de palavras.-> numero total de palavras unicas dividido pelo 
	numero total de palavras
	
    Tamanho médio de sentença: Média simples do número de caracteres por sentença.-> numero total de caracteres dividido pelo numero de sentencas
	
    Complexidade de sentença: Média simples do número de frases por sentença. -> calculo do numero todal de frases dividido pelo numero toral de sentencas
	
    Tamanho médio de frase: Média simples do número de caracteres por frase. -> calculo do numero total de caracteres dividido por numero total de frases
	
	Funcionamento do programa

Diversos estudos foram compilados e hoje se conhece precisamente a assinatura de um portador de COH-PIAH. Seu programa deverá receber diversos textos e 
calcular os valores dos diferentes traços linguísticos da seguinte forma:

    Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
	
    Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 
	palavras no total (o, gato, caçava, o, rato) mas somente 4 diferentes (o, gato, caçava, rato). Nessa frase, a relação Type-Token vale 45=0.8
	
    Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras. Por exemplo, na frase "O gato caçava o 
	rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 3 que aparecem só uma vez (gato, caçava, rato). Nessa frase, a relação 
	Hapax Legomana vale 35=0.6
	
    Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças (os caracteres que separam 
	uma sentença da outra não devem ser contabilizados como parte da sentença).
	
    Complexidade de sentença é o número total de frases divido pelo número de sentenças.
	
    Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto (os caracteres que separam uma frase 
	da outra não devem ser contabilizados como parte da frase).

Após calcular esses valores para cada texto, você deve comparar com a assinatura fornecida para os infectados por COH-PIAH. O grau de similaridade 
entre dois textos, a e b, é dado pela fórmula:

Sab=∑i=16||fi,a−fi,b||6

Onde:

    Sab é o grau de similaridade entre os textos a e b;
    fi,a é o valor de cada traço linguístico i no texto a; e
    fi,b é o valor de cada traço linguístico i no texto b.

Perceba que quanto mais similares a e b forem, menor Sab será. Para cada texto, você deve calcular o grau de similaridade com a assinatura do portador 
de COH-PIAH e no final exibir qual o texto que mais provavelmente foi escrito por algum aluno infectado.Perceba
'''
#TODO ESCREVER FUNCOES PARA CALCULO DOS PARAMETROS
#TODO DESCOBRIR O NUMERO TOTAL DE LETRAS
#TODO DESCOBRIR O NUMERO TOTAL DE PALAVRAS DO TEXTO
#TODO DESCOBRI O NUMERO TOTAL DE FRASES
#TODO DESCOBRIR O NUMERO TOTAL DE SENTENCAS
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
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do
    texto.'''
    pass

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o
    numero (1 a n) do texto com maior probabilidade de ter sido infectado
    por COH-PIAH.'''
    pass

    

def main0():
    #textos = le_textos()# faz a leitura dos textos e armazena em textos
    #textos = ['(1)Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.','(2)Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.','(3)NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.']
    #textos = ['a 1, oi teu bem. ola','b 2, teste .paranaue','c 3, teste1 .gingolo']
    textos = ['a b c','a b c']
    print('quantidade de textos ',len(textos))
    print(textos)
    sentencas = []
    cont = 0
    print('separando textos')
    for texto in textos:
        sentencas.append(separa_sentencas(texto))
        cont += 1
    print(sentencas)
    print('quantidade de sentencas ',cont)
    cont = 0
    frases_fora = []
    frases_dentro = []
    frases = []
    for frases_fora in sentencas:
        for frases_dentro in frases_fora:
            frases.append(separa_frases(frases_dentro))
            cont += 1
    print(frases)
    print('quantidade de frases ', cont)
    cont = 0
    palavras = []
    palavra_fora = []
    palavra_dentro = []
    
    for palavra_fora in frases:
        for palavra_dentro in palavra_fora:
            palavras.append(separa_palavras(palavra_dentro))
            cont += 1
    print(palavras)
    print('quantidade de palavras ', cont)
    
def main1():
	# textos = le_textos()# faz a leitura dos textos e armazena em textos
	#textos = ['(1)Navegadores antigos tinham uma frase gloriosa:"Navegar eh preciso; viver nao eh preciso". Quero para mim o espirito [d]esta frase, transformada a forma para a casar como eu sou: Viver nao eh necessario; o que eh necessario eh criar. Nao conto gozar a minha vida; nem em goza-la penso. So quero torna-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. So quero torna-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essencia animica do meu sangueo proposito impessoal de engrandecer a patria e contribuirpara a evolucao da humanidade.Eh a forma que em mim tomou o misticismo da nossa Raca.','(2)Voltei-me para ela; Capitu tinha os olhos no chao. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissao de criancas, tu valias bem duas ou tres paginas, mas quero ser poupado. Em verdade, nao falamos nada; o muro falou por nos. Nao nos movemos, as maos e que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Nao marquei a hora exata daquele gesto. Devia te-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas nao traria nenhum, tal era a diferenca entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.','(3)NOSSA alegria diante dum sistema metafisico, nossa satisfacao em presenca duma construcao do pensamento, em que a organizacao espiritual do mundo se mostra num conjunto logico, coerente a harmonico, sempre dependem eminentemente da estetica; tem a mesma origem que o prazer, que a alta satisfacao, sempre serena afinal, que a atividade artistica nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparencia.']
	#textos = ['a 1, oi teu bem. ola','b 2, teste .paranaue','c 3, teste1 .gingolo']
	textos = ['ola, este eh um teste. Bom dia hoje vamos ter linhas de programacao sendo digitadas, e quando isso acontence temos diversao.','Hoje o dia amanheceu assim, como assim, se eh mesmo assim. A vida nos leva a cada coisa estranha, parece que o mundo da voltas e mais voltas']
	print('quantidade de textos ', len(textos))
	print(textos)
	print('***************************************')
	cont_texto = 0
	cont_sentenca = 0
	cont_frase = 0
	cont_palavra = 0
	for texto in textos:
		print('**************----inicio------******************')
		print('texto ', cont_texto, ' -> ',texto)
		cont_texto += 1
		sentencas = separa_sentencas(texto)
		for sentenca in sentencas:
			print('sentencas ', cont_sentenca, ' -> ',sentencas)
			cont_sentenca += 1
			frases = separa_frases(sentenca)
			for frase in frases:
				print('frases  ', cont_frase, ' -> ',frases)
				cont_frase += 1
				palavras = separa_palavras(frase)
				unicas = n_palavras_unicas(palavras)
				diferentes = n_palavras_diferentes(palavras)
				print('palavras ', cont_palavra, ' -> ',palavras)
				cont_palavra += 1
				print(unicas)
				print(diferentes)
				print('**************------fim--------******************')
				
main1()