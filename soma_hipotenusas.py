'''
Exercício 2 - (Difícil) Soma das hipotenusas

Escreva uma função soma_hipotenusas que receba como parâmetro um número
inteiro positivo n e devolva a soma de todos os inteiros entre 1 e n que
são comprimento da hipotenusa de algum triângulo retângulo com catetos
inteiros.

DIca1: um mesmo número pode ser hipotenusa de vários triângulos, mas deve
ser somado apenas uma vez. Uma boa solução para este exercício é fazer um
laço de 1 até n testando se o número é hipotenusa de algum triângulo e
somando em caso afirmativo. Uma solução que dificilmente vai dar certo é
fazer um laço construindo triângulos e somando as hipotenusas inteiras
encontradas.

Dica2: primeiro faça uma função é_hipotenusa que diz se um número inteiro
é o comprimento da hipotenusa de um triângulo com lados de comprimento
inteiro ou não.

Exemplo:
# Para n = 25, as hipotenusas são:
# 5, 10, 13, 15, 17, 20, 25
# note que cada número deve ser somado apenas uma vez. Assim:
soma_hipotenusas(25)
# deve devolver 105
'''

def soma_hipotenusas(n):
    soma = 1
    hipo = 0
    while soma < n:
        if é_hipotenusa(soma):
            hipo += soma
        soma += 1
    return soma

def é_hipotenusa(n):
    from math import sqrt
    ca = 1
    co = 1
    hipo = False
    while ca <= n:#loop cateto adjacente
        while co <= n: #loop cateto oposto
            hipotenusa = sqrt(ca ** 2 + co ** 2)
            if n == hipotenusa:
                print('hipotenusa: {} cateto adjacente {} cateto oposto {}'.format(hipotenusa, ca ,co))
                hipo = True
            co += 1
        co = 1
        ca += 1
    return hipo
    
n = int(input('eh hipotenusa: '))

é_hipotenusa(n)
print(soma_hipotenusas(n))