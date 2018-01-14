# somar os digitos de um numero
# ex: 123 = 1+2+3 = 6


numero = int(input('Digite um numero: '))

soma = 0
if numero != 0:
    while numero // 10 != 0:
        soma += numero % 10
        print('valor da soma {}'.format(soma))
        numero = numero // 10
    soma += numero % 10
else:
    soma = numero
print('A soma dos digitos é {}'.format(soma))