#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#considerar US$ 1.00 = R$ 3.27
dinheiro = float(input('Digite quanto de dinherio voce tem: '))
print('Voce pode comprar {:.2f} dolares'.format(dinheiro/3.27))