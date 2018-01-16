#2, 3, 5, 7, 11 ...

'''
algoritimo generico para descobrir numeros primos
ler um numero inteiro positivo

'''

primalidade = True
primo = 'é'

#numero = int(input('Digite um numero interio positivo: '))
numero = 15
print('1')

while True:
    #numero = numero + 1
    i = 2
    while i != numero:
        if numero % i == 0:
            primalidade = False
            primo = 'não é'
        i = i + 1
        print(' i - ',i)
       
    if primalidade:
        print(numero)
    primalidade = True